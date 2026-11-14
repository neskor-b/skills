from __future__ import annotations

import importlib.util
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = SKILL_ROOT / "scripts" / "render_cv.py"
FIXTURES = Path(__file__).resolve().parent / "fixtures"
try:
    import pdfplumber  # noqa: F401
    import pypdf  # noqa: F401
    import reportlab  # noqa: F401

    PDF_DEPS_AVAILABLE = True
except ModuleNotFoundError:
    PDF_DEPS_AVAILABLE = False


def load_renderer():
    spec = importlib.util.spec_from_file_location("cv_render_cv", SCRIPT_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load renderer from {SCRIPT_PATH}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


class ParseCvMarkdownTests(unittest.TestCase):
    def test_parses_supported_blocks_in_order(self):
        renderer = load_renderer()
        source = (FIXTURES / "one-page.md").read_text(encoding="utf-8")

        document = renderer.parse_cv_markdown(source)

        self.assertEqual(document.blocks[0].kind, "title")
        self.assertEqual(document.blocks[0].text, "Alex Morgan")
        self.assertEqual(document.blocks[1].kind, "subtitle")
        self.assertEqual(document.blocks[2].kind, "contact")
        self.assertIn("heading", [block.kind for block in document.blocks])
        self.assertIn("paragraph", [block.kind for block in document.blocks])
        self.assertIn("bullet", [block.kind for block in document.blocks])
        self.assertEqual(
            [block.text for block in document.blocks],
            [block.text for block in sorted(document.blocks, key=lambda block: block.order)],
        )

    def test_rejects_empty_document(self):
        renderer = load_renderer()
        with self.assertRaisesRegex(ValueError, "empty"):
            renderer.parse_cv_markdown(" \n")

    def test_rejects_images(self):
        renderer = load_renderer()
        with self.assertRaisesRegex(ValueError, "images"):
            renderer.parse_cv_markdown("# Name\n![Photo](photo.png)\n")

    def test_rejects_markdown_tables(self):
        renderer = load_renderer()
        with self.assertRaisesRegex(ValueError, "tables"):
            renderer.parse_cv_markdown("# Name\n| Skill | Years |\n| --- | --- |\n")

    def test_rejects_nested_bullets(self):
        renderer = load_renderer()
        with self.assertRaisesRegex(ValueError, "Nested bullets"):
            renderer.parse_cv_markdown("# Name\n- Parent\n  - Child\n")

    def test_rejects_markdown_links_in_favor_of_textual_urls(self):
        renderer = load_renderer()
        with self.assertRaisesRegex(ValueError, "Markdown links"):
            renderer.parse_cv_markdown("# Name\nRole\n[GitHub](https://github.com/name)\n")

    def test_rejects_html(self):
        renderer = load_renderer()
        with self.assertRaisesRegex(ValueError, "HTML"):
            renderer.parse_cv_markdown("# Name\nRole\n<div>Hidden layout</div>\n")

@unittest.skipUnless(PDF_DEPS_AVAILABLE, "PDF dependencies are not installed in this Python runtime")
class RenderCvTests(unittest.TestCase):
    def assert_fixture_renders(self, fixture_name: str, expected_pages: int):
        renderer = load_renderer()
        source = (FIXTURES / fixture_name).read_text(encoding="utf-8")
        document = renderer.parse_cv_markdown(source)

        with tempfile.TemporaryDirectory() as temp_dir:
            output = Path(temp_dir) / f"{Path(fixture_name).stem}.pdf"
            renderer.render_cv(document, output)
            extracted = renderer.extract_pdf_text(output)
            renderer.verify_content(document, extracted)

            from pypdf import PdfReader

            reader = PdfReader(str(output))
            self.assertEqual(len(reader.pages), expected_pages)
            self.assertTrue(all(page.get_contents() is not None for page in reader.pages))
            self.assertIn("https://github.com/", extracted)
            link_targets = []
            for page in reader.pages:
                for annotation_ref in page.get("/Annots", []):
                    annotation = annotation_ref.get_object()
                    action = annotation.get("/A")
                    if action and action.get("/URI"):
                        link_targets.append(action["/URI"])
            self.assertTrue(
                any(target.startswith("https://github.com/") for target in link_targets),
                "Expected a clickable GitHub URL annotation",
            )
            embedded_font_found = False
            for page in reader.pages:
                resources = page["/Resources"]
                for font_ref in resources.get("/Font", {}).values():
                    font = font_ref.get_object()
                    descriptor_ref = font.get("/FontDescriptor")
                    if descriptor_ref is None and font.get("/DescendantFonts"):
                        descendant = font["/DescendantFonts"][0].get_object()
                        descriptor_ref = descendant.get("/FontDescriptor")
                    if descriptor_ref is None:
                        continue
                    descriptor = descriptor_ref.get_object()
                    if any(key in descriptor for key in ("/FontFile", "/FontFile2", "/FontFile3")):
                        embedded_font_found = True
            self.assertTrue(embedded_font_found, "Expected at least one embedded font")

    def test_renders_one_page_fixture(self):
        self.assert_fixture_renders("one-page.md", 1)

    def test_renders_two_page_fixture(self):
        self.assert_fixture_renders("two-page.md", 2)

    def test_verify_content_rejects_unapproved_inserted_text(self):
        renderer = load_renderer()
        document = renderer.parse_cv_markdown("# Alex Morgan\nBackend Engineer\n")
        with self.assertRaisesRegex(ValueError, "does not exactly match"):
            renderer.verify_content(document, "Alex Morgan\nInvented claim\nBackend Engineer")

    def test_cli_failure_does_not_leave_output(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            invalid_input = temp_path / "invalid.md"
            output = temp_path / "invalid.pdf"
            invalid_input.write_text("# Name\n| Bad | Table |\n| --- | --- |\n", encoding="utf-8")

            result = subprocess.run(
                [sys.executable, str(SCRIPT_PATH), str(invalid_input), str(output)],
                capture_output=True,
                text=True,
                check=False,
            )

            self.assertNotEqual(result.returncode, 0)
            self.assertIn("Markdown tables", result.stderr)
            self.assertFalse(output.exists())

    def test_cli_success_writes_verified_output(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            output = Path(temp_dir) / "verified.pdf"

            result = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT_PATH),
                    str(FIXTURES / "one-page.md"),
                    str(output),
                ],
                capture_output=True,
                text=True,
                check=False,
            )

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertTrue(output.exists())
            self.assertIn("(1 page)", result.stdout)

    def test_rendered_text_lines_do_not_overlap_or_cross_margins(self):
        import pdfplumber

        renderer = load_renderer()
        source = (FIXTURES / "two-page.md").read_text(encoding="utf-8")
        document = renderer.parse_cv_markdown(source)

        with tempfile.TemporaryDirectory() as temp_dir:
            output = Path(temp_dir) / "layout.pdf"
            renderer.render_cv(document, output)

            with pdfplumber.open(output) as pdf:
                for page in pdf.pages:
                    lines = page.extract_text_lines(layout=False, return_chars=False)
                    self.assertTrue(lines)
                    self.assertGreaterEqual(min(line["top"] for line in lines), 39.0)
                    self.assertLessEqual(max(line["bottom"] for line in lines), page.height - 39.0)
                    for previous, current in zip(lines, lines[1:]):
                        self.assertLessEqual(
                            previous["bottom"],
                            current["top"] + 0.25,
                            f"Text lines overlap: {previous['text']} / {current['text']}",
                        )


if __name__ == "__main__":
    unittest.main()
