"""Render a paper .md file to PDF with reportlab (no pandoc on this VM).
Usage: python3 md2pdf.py <input.md> <output.pdf>
Handles: # / ## / ### headings, paragraphs, **bold**, *italic*, markdown
tables (| ... |), horizontal rules, bullet-ish lines. Keeps it simple and
deterministic; tables use a small font so wide tables fit A4.
"""
import re
import sys

import markdown
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer,
                                Table, TableStyle, HRFlowable, PageBreak)

STYLES = {
    "title": ParagraphStyle("title", fontName="Helvetica-Bold", fontSize=17,
                            leading=21, spaceAfter=6, alignment=1),
    "h1": ParagraphStyle("h1", fontName="Helvetica-Bold", fontSize=14,
                         leading=18, spaceBefore=14, spaceAfter=6),
    "h2": ParagraphStyle("h2", fontName="Helvetica-Bold", fontSize=12,
                         leading=15, spaceBefore=10, spaceAfter=4),
    "h3": ParagraphStyle("h3", fontName="Helvetica-BoldOblique", fontSize=11,
                         leading=14, spaceBefore=8, spaceAfter=3),
    "body": ParagraphStyle("body", fontName="Helvetica", fontSize=10.5,
                           leading=14.5, spaceAfter=6, alignment=4),
    "cell": ParagraphStyle("cell", fontName="Helvetica", fontSize=8.5,
                           leading=11, spaceAfter=0),
    "cellb": ParagraphStyle("cellb", fontName="Helvetica-Bold", fontSize=8.5,
                            leading=11, spaceAfter=0),
    "cellh": ParagraphStyle("cellh", fontName="Helvetica-Bold", fontSize=8.5,
                            leading=11, spaceAfter=0, textColor=colors.white),
}


def md_inline(text):
    """Convert a markdown inline fragment to reportlab paragraph markup."""
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"\*(.+?)\*", r"<i>\1</i>", text)
    text = re.sub(r"`(.+?)`", r"<font face='Courier' size='9'>\1</font>", text)
    text = re.sub(r"\[(.+?)\]\(.+?\)", r"\1", text)
    return text


def split_row(line):
    cells = [c.strip() for c in line.strip().strip("|").split("|")]
    return cells


def build_table(lines):
    header = split_row(lines[0])
    rows = [split_row(l) for l in lines[2:] if l.strip().startswith("|")]
    data = [[Paragraph(md_inline(c), STYLES["cellh"]) for c in header]]
    for r in rows:
        data.append([Paragraph(md_inline(c), STYLES["cell"]) for c in r])
    ncol = len(header)
    widths = [None] * ncol
    t = Table(data, colWidths=widths, repeatRows=1, hAlign="CENTER")
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1f3864")),
        ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#888888")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1),
         [colors.white, colors.HexColor("#eef2f8")]),
    ]))
    return t


def main(src, dst):
    lines = open(src, encoding="utf-8").read().splitlines()
    story = []
    i = 0
    first_h1 = True
    while i < len(lines):
        line = lines[i]
        if line.startswith("|") and i + 1 < len(lines) and re.match(
                r"^\|[\s\-:|]+\|$", lines[i + 1]):
            block = [line, lines[i + 1]]
            i += 2
            while i < len(lines) and lines[i].strip().startswith("|"):
                block.append(lines[i])
                i += 1
            story.append(build_table(block))
            story.append(Spacer(1, 6))
            continue
        if line.startswith("# "):
            style = STYLES["title"] if first_h1 else STYLES["h1"]
            first_h1 = False
            story.append(Paragraph(md_inline(line[2:].strip()), style))
        elif line.startswith("## "):
            story.append(Paragraph(md_inline(line[3:].strip()), STYLES["h2"]))
        elif line.startswith("### "):
            story.append(Paragraph(md_inline(line[4:].strip()), STYLES["h3"]))
        elif line.strip() == "---":
            story.append(HRFlowable(width="100%", thickness=0.6,
                                    color=colors.HexColor("#888888"),
                                    spaceBefore=4, spaceAfter=8))
        elif line.strip() == "":
            pass
        elif line.strip().startswith("- ") or re.match(r"^\d+\. ", line.strip()):
            story.append(Paragraph("•  " + md_inline(
                re.sub(r"^(\-|\d+\.)\s+", "", line.strip())), STYLES["body"]))
        else:
            # Join wrapped lines into one paragraph.
            para = [line]
            i += 1
            while (i < len(lines) and lines[i].strip() != ""
                   and not lines[i].startswith(("#", "|", "- "))
                   and not re.match(r"^\d+\. ", lines[i].strip())):
                para.append(lines[i])
                i += 1
            story.append(Paragraph(md_inline(" ".join(p.strip() for p in para)),
                                   STYLES["body"]))
            continue
        i += 1

    def footer(canvas, doc):
        canvas.saveState()
        canvas.setFont("Helvetica", 8)
        canvas.setFillColor(colors.HexColor("#666666"))
        canvas.drawCentredString(A4[0] / 2, 1.2 * cm,
                                 f"AI-assisted draft — NOT peer-reviewed, NOT published  ·  page {doc.page}")
        canvas.restoreState()

    doc = SimpleDocTemplate(dst, pagesize=A4,
                            leftMargin=2 * cm, rightMargin=2 * cm,
                            topMargin=1.8 * cm, bottomMargin=1.8 * cm,
                            title="Daily research paper",
                            author="Zubair Ali")
    doc.build(story, onFirstPage=footer, onLaterPages=footer)
    print("Wrote", dst)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
