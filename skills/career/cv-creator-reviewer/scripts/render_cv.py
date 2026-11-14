#!/usr/bin/env python3
"""Render an approved, constrained Markdown CV as an ATS-safe PDF."""

from __future__ import annotations

import argparse
import html
import os
import re
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List

PDF_IMPORT_ERROR = None
try:
    import reportlab
    from pypdf import PdfReader
    from reportlab.lib import colors
    from reportlab.lib.enums import TA_CENTER, TA_LEFT
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
    from reportlab.lib.units import mm
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.platypus import (
        BaseDocTemplate,
        Frame,
        KeepTogether,
        PageTemplate,
        Paragraph,
        Spacer,
    )
except ModuleNotFoundError as exc:
    PDF_IMPORT_ERROR = exc


ALLOWED_KINDS = {"title", "subtitle", "contact", "heading", "paragraph", "bullet"}
DASH_TRANSLATION = str.maketrans({"\u2011": "-", "\u2013": "-", "\u2014": "-"})
URL_RE = re.compile(r"https?://[^\s|<>]+")
BOLD_RE = re.compile(r"\*\*(.+?)\*\*")


@dataclass(frozen=True)
class Block:
    order: int
    kind: str
    text: str
    markup: str
    emphasis: bool = False

    def __post_init__(self) -> None:
        if self.kind not in ALLOWED_KINDS:
            raise ValueError(f"Unsupported block kind: {self.kind}")


@dataclass(frozen=True)
class CvDocument:
    blocks: List[Block]


def _normalize_dashes(value: str) -> str:
    return value.translate(DASH_TRANSLATION)


def _plain_text(value: str) -> str:
    value = _normalize_dashes(value)
    value = BOLD_RE.sub(r"\1", value)
    value = re.sub(r"\[([^\]]+)\]\((https?://[^)]+)\)", r"\1 (\2)", value)
    value = value.replace("\\", "")
    return value.strip()


def parse_cv_markdown(source: str) -> CvDocument:
    """Parse the small Markdown subset accepted by the CV renderer."""

    if not source.strip():
        raise ValueError("CV Markdown is empty")
    if re.search(r"!\[[^\]]*\]\([^)]+\)", source):
        raise ValueError("Markdown images are not supported")
    if re.search(r"(?<!!)\[[^\]]+\]\(https?://[^)]+\)", source):
        raise ValueError("Markdown links are not supported; use bare textual URLs")
    if re.search(r"(?m)^\s*<[^>]+>", source):
        raise ValueError("HTML is not supported")

    lines = source.splitlines()
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("|") and stripped.endswith("|"):
            raise ValueError("Markdown tables are not supported")
        if re.match(r"^\s{2,}[-*+]\s+", line):
            raise ValueError("Nested bullets are not supported")

    blocks: List[Block] = []
    title_seen = False
    subtitle_seen = False
    section_seen = False

    def append(kind: str, markup: str, *, emphasis: bool = False) -> None:
        text = _plain_text(markup)
        if text:
            blocks.append(Block(len(blocks), kind, text, _normalize_dashes(markup), emphasis))

    for raw_line in lines:
        line = raw_line.strip()
        if not line or line == "---":
            continue
        if line.startswith("# "):
            if title_seen or blocks:
                raise ValueError("The document must contain one leading level-one title")
            append("title", line[2:])
            title_seen = True
            continue
        if not title_seen:
            raise ValueError("The first content line must be a level-one title")
        if line.startswith("## "):
            append("heading", line[3:])
            section_seen = True
            continue
        if line.startswith("### "):
            append("paragraph", line[4:], emphasis=True)
            continue
        if line.startswith("- "):
            append("bullet", line[2:])
            continue
        if re.match(r"^[*+]\s+", line):
            raise ValueError("Only standard '-' bullets are supported")
        if not subtitle_seen:
            append("subtitle", line)
            subtitle_seen = True
        elif not section_seen and ("|" in line or URL_RE.search(line)):
            append("contact", line)
        else:
            append("paragraph", line)

    if not blocks or blocks[0].kind != "title":
        raise ValueError("The document requires a title")
    return CvDocument(blocks)


def _register_font() -> tuple[str, str]:
    _require_pdf_dependencies()
    reportlab_fonts = Path(reportlab.__file__).resolve().parent / "fonts"
    candidates = [
        Path("/System/Library/Fonts/Supplemental/Arial.ttf"),
        Path("/Library/Fonts/Arial.ttf"),
        Path("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"),
        reportlab_fonts / "Vera.ttf",
    ]
    bold_candidates = [
        Path("/System/Library/Fonts/Supplemental/Arial Bold.ttf"),
        Path("/Library/Fonts/Arial Bold.ttf"),
        Path("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"),
        reportlab_fonts / "VeraBd.ttf",
    ]
    regular = next((path for path in candidates if path.exists()), None)
    bold = next((path for path in bold_candidates if path.exists()), None)
    if regular and bold:
        pdfmetrics.registerFont(TTFont("CVSans", str(regular)))
        pdfmetrics.registerFont(TTFont("CVSans-Bold", str(bold)))
        pdfmetrics.registerFontFamily(
            "CVSans", normal="CVSans", bold="CVSans-Bold", italic="CVSans", boldItalic="CVSans-Bold"
        )
        return "CVSans", "CVSans-Bold"
    raise RuntimeError(
        "No embeddable CV font found. Install Arial or DejaVu Sans, "
        "or reinstall ReportLab with its bundled Vera fonts."
    )


def _require_pdf_dependencies() -> None:
    if PDF_IMPORT_ERROR is not None:
        raise RuntimeError(
            "PDF dependencies are missing. Use the Codex bundled PDF runtime or install "
            "'reportlab' and 'pypdf' for this Python interpreter."
        ) from PDF_IMPORT_ERROR


def _paragraph_markup(block: Block) -> str:
    source = block.markup
    placeholders: List[str] = []

    def stash_bold(match: re.Match[str]) -> str:
        placeholders.append(f"<b>{html.escape(match.group(1))}</b>")
        return f"\x00BOLD{len(placeholders) - 1}\x00"

    source = BOLD_RE.sub(stash_bold, source)
    escaped = html.escape(source)
    for index, replacement in enumerate(placeholders):
        escaped = escaped.replace(f"\x00BOLD{index}\x00", replacement)

    def link_url(match: re.Match[str]) -> str:
        url = match.group(0)
        escaped_url = html.escape(url, quote=True)
        return f'<link href="{escaped_url}" color="#1F4E79">{html.escape(url)}</link>'

    escaped = URL_RE.sub(link_url, escaped)
    if block.emphasis:
        escaped = f"<b>{escaped}</b>"
    return escaped


def _styles():
    regular_font, bold_font = _register_font()
    base = getSampleStyleSheet()
    return {
        "title": ParagraphStyle(
            "CVTitle",
            parent=base["Title"],
            fontName=bold_font,
            fontSize=21,
            leading=24,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#142B3D"),
            spaceAfter=2.5 * mm,
        ),
        "subtitle": ParagraphStyle(
            "CVSubtitle",
            parent=base["Normal"],
            fontName=bold_font,
            fontSize=11.5,
            leading=14,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#33566F"),
            spaceAfter=1.5 * mm,
        ),
        "contact": ParagraphStyle(
            "CVContact",
            parent=base["Normal"],
            fontName=regular_font,
            fontSize=9.5,
            leading=12,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#263746"),
            spaceAfter=1.2 * mm,
        ),
        "heading": ParagraphStyle(
            "CVHeading",
            parent=base["Heading2"],
            fontName=bold_font,
            fontSize=11.5,
            leading=14,
            alignment=TA_LEFT,
            textColor=colors.HexColor("#142B3D"),
            borderWidth=0,
            borderPadding=0,
            spaceBefore=3.2 * mm,
            spaceAfter=1.4 * mm,
            keepWithNext=True,
        ),
        "paragraph": ParagraphStyle(
            "CVParagraph",
            parent=base["BodyText"],
            fontName=regular_font,
            fontSize=9.5,
            leading=12.3,
            alignment=TA_LEFT,
            textColor=colors.HexColor("#1F2933"),
            spaceAfter=1.2 * mm,
        ),
        "bullet": ParagraphStyle(
            "CVBullet",
            parent=base["BodyText"],
            fontName=regular_font,
            fontSize=9.5,
            leading=12.3,
            leftIndent=4.5 * mm,
            firstLineIndent=-3.2 * mm,
            bulletIndent=0,
            textColor=colors.HexColor("#1F2933"),
            spaceAfter=1.1 * mm,
        ),
    }


def _flowable(block: Block, styles):
    markup = _paragraph_markup(block)
    if block.kind == "bullet":
        return Paragraph(markup, styles["bullet"], bulletText="\u2022")
    return Paragraph(markup, styles[block.kind])


def _story(blocks: Iterable[Block], styles):
    block_list = list(blocks)
    story = []
    index = 0
    while index < len(block_list):
        block = block_list[index]
        item = _flowable(block, styles)
        if block.kind == "heading" and index + 1 < len(block_list):
            first = _flowable(block_list[index + 1], styles)
            story.append(KeepTogether([item, first]))
            index += 2
            continue
        story.append(item)
        index += 1
    story.append(Spacer(1, 0.5 * mm))
    return story


def render_cv(document: CvDocument, output_path: Path) -> None:
    """Render a parsed CV document to a single-column A4 PDF."""

    _require_pdf_dependencies()
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    styles = _styles()
    document_template = BaseDocTemplate(
        str(output_path),
        pagesize=A4,
        leftMargin=16 * mm,
        rightMargin=16 * mm,
        topMargin=14 * mm,
        bottomMargin=14 * mm,
        title=document.blocks[0].text,
        author=document.blocks[0].text,
    )
    frame = Frame(
        document_template.leftMargin,
        document_template.bottomMargin,
        document_template.width,
        document_template.height,
        id="cv-body",
        leftPadding=0,
        rightPadding=0,
        topPadding=0,
        bottomPadding=0,
    )
    document_template.addPageTemplates([PageTemplate(id="cv", frames=[frame])])
    document_template.build(_story(document.blocks, styles))


def extract_pdf_text(path: Path) -> str:
    _require_pdf_dependencies()
    reader = PdfReader(str(path))
    return "\n".join((page.extract_text() or "") for page in reader.pages)


def _normalize_for_compare(value: str) -> str:
    return re.sub(r"\s+", " ", _normalize_dashes(value)).strip()


def verify_content(document: CvDocument, extracted_text: str) -> None:
    """Require the extracted visible text to equal the approved block stream."""

    approved = _normalize_for_compare(" ".join(block.text for block in document.blocks))
    normalized_pdf = _normalize_for_compare(extracted_text.replace("\x7f", " "))
    if normalized_pdf != approved:
        raise ValueError("Extracted PDF text does not exactly match the approved CV content")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input_markdown", type=Path)
    parser.add_argument("output_pdf", type=Path)
    args = parser.parse_args(argv)

    temp_path = None
    try:
        source = args.input_markdown.read_text(encoding="utf-8")
        document = parse_cv_markdown(source)
        output_parent = args.output_pdf.parent
        output_parent.mkdir(parents=True, exist_ok=True)
        with tempfile.NamedTemporaryFile(
            prefix=f".{args.output_pdf.stem}-",
            suffix=".pdf",
            dir=output_parent,
            delete=False,
        ) as temp_file:
            temp_path = Path(temp_file.name)
        render_cv(document, temp_path)
        extracted = extract_pdf_text(temp_path)
        verify_content(document, extracted)
        page_count = len(PdfReader(str(temp_path)).pages)
        os.replace(temp_path, args.output_pdf)
        temp_path = None
    except Exception as exc:
        if temp_path is not None:
            temp_path.unlink(missing_ok=True)
        print(f"error: {exc}", file=sys.stderr)
        return 1

    print(f"{args.output_pdf.resolve()} ({page_count} page{'s' if page_count != 1 else ''})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
