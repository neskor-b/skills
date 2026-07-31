from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = SKILL_ROOT / "scripts" / "render_cv.py"
FIXTURES = Path(__file__).resolve().parent / "fixtures"


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

    def test_renders_one_page_fixture(self):
        self.assert_fixture_renders("one-page.md", 1)

    def test_renders_two_page_fixture(self):
        self.assert_fixture_renders("two-page.md", 2)


if __name__ == "__main__":
    unittest.main()
