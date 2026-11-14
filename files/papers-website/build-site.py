#!/usr/bin/env python3
"""Regenerate the research-papers website from the manuscripts in files/.

Run from this folder (files/papers-website/) or anywhere:
    python3 build-site.py
Reads ../2026-*.md + ../leadforge-manuscript-v1.md + the health-papers
tracker, extracts title + abstract, converts each full manuscript from
Markdown to HTML, and writes:
  - papers-data.json : manifest (title/date/field/abstract/status/files)
  - site.html        : self-contained page — all papers grouped by field,
                       newest first, abstract on the card, full text inside
                       a collapsible "Read full paper" section, client-side
                       search + field filter. Re-run after every daily
                       papers run to pick up new manuscripts.
The artifact website (slug zubair-research-papers) is built from site.html.
"""
import argparse
import html
import json
import re
import shutil
from datetime import date
from pathlib import Path

import markdown

HERE = Path(__file__).resolve().parent
FILES = HERE.parent
TRACKER = HERE.parent.parent / "hidden_files" / "health-papers-tracker.json"
SANDBOX = "sandbox://workspace/goals/pharmacy-research-paper-team-daily-digest-and-manuscripts/files/"
# Default link base for the Muse artifact build. --pages-dir switches to
# relative "papers/" links for the public GitHub Pages build.
LINK_BASE = SANDBOX

SUPERSEDED = {
    "2026-11-02-health-thymoquinone-aldose-reductase.md": "Superseded by v2 (4 Nov 2026)",
    "2026-11-02-health-dual-ar-sglt2.md": "Superseded by v2 (4 Nov 2026)",
}
READY = {
    "2026-11-04-health-thymoquinone-aldose-reductase-v2.md": "v2 — ready to submit",
    "2026-11-04-health-dual-ar-sglt2-v2.md": "v2 — ready to submit",
}
TRACK_LABEL = {"health": "Health", "brain": "Brain", "space": "Space",
               "natural": "Natural Science", "social": "Social Science",
               "drugdiscovery": "Drug Discovery"}
FIELDS = ("health", "brain", "space", "natural", "social", "drugdiscovery")

MD = markdown.Markdown(extensions=["tables", "fenced_code"])


def title_of(text: str, fallback: str) -> str:
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return fallback


def abstract_of(text: str) -> str:
    m = re.search(r"## Abstract\s*\n+(.*?)(?=\n## |\n\*\*Keywords\*\*|\n---\n)", text, re.S)
    if not m:
        return ""
    abs_text = re.sub(r"\s+", " ", m.group(1)).strip()
    abs_text = re.sub(r"\*\*([^*]+)\*\*", r"\1", abs_text)
    abs_text = re.sub(r"\*([^*]+)\*", r"\1", abs_text)
    return abs_text


def summary_of(abs_text: str, limit: int = 320) -> str:
    if len(abs_text) <= limit:
        return abs_text
    cut = abs_text[:limit]
    dot = cut.rfind(". ")
    if dot > 120:
        return cut[: dot + 1]
    return cut.rstrip() + "…"


def body_html(text: str) -> str:
    # Drop the H1 title (shown in the card header) but keep everything
    # else, including the AI-assisted-draft disclaimer line.
    lines = text.splitlines()
    if lines and lines[0].startswith("# "):
        lines = lines[1:]
    MD.reset()
    return MD.convert("\n".join(lines))


def status_of(name: str, tracker_status: str) -> str:
    if name in SUPERSEDED:
        return SUPERSEDED[name]
    if name in READY:
        return READY[name]
    if tracker_status == "submitted":
        return "Submitted to ChemRxiv — rejected, see v2"
    if tracker_status == "draft-ready":
        return "Draft ready"
    if tracker_status == "draft-partial":
        return "Partial draft"
    return "Draft — not submitted"


def collect():
    tracker = {}
    if TRACKER.exists():
        data = json.loads(TRACKER.read_text(encoding="utf-8"))
        for p in data.get("papers", []):
            f = p.get("file", "")
            if f:
                tracker[Path(f).name] = p
    papers = []
    for path in sorted(FILES.glob("2026-*.md"), reverse=True):
        m = re.match(r"(2026-\d\d-\d\d)-(health|brain|space|natural|social|drugdiscovery)-", path.name)
        if not m:
            continue
        date, track = m.group(1), m.group(2)
        text = path.read_text(encoding="utf-8", errors="replace")
        papers.append({
            "date": date, "field": track,
            "title": title_of(text, path.stem),
            "abstract": abstract_of(text),
            "md": path.name, "pdf": path.with_suffix(".pdf").name,
            "status": status_of(path.name, tracker.get(path.name, {}).get("status", "")),
            "body_html": body_html(text),
        })
    lf = FILES / "leadforge-manuscript-v1.md"
    if lf.exists():
        text = lf.read_text(encoding="utf-8", errors="replace")
        papers.append({
            "date": "2026-10-07", "field": "health",
            "title": title_of(text, lf.stem),
            "abstract": abstract_of(text),
            "md": lf.name, "pdf": "leadforge-manuscript-v1.pdf",
            "status": "Draft — not submitted",
            "body_html": body_html(text),
        })
    return papers


def card(p: dict, idx: int) -> str:
    summ = html.escape(summary_of(p["abstract"]))
    title = html.escape(p["title"])
    status = html.escape(p["status"])
    return f"""<article class="card" data-field="{p['field']}" data-title="{html.escape(p['title'].lower())}">
<div class="meta"><span class="date">{p['date']}</span> <span class="badge {p['field']}">{TRACK_LABEL[p['field']]}</span> <span class="status">{status}</span></div>
<h3>{title}</h3>
<p class="abs">{summ}</p>
<p class="links"><a href="{LINK_BASE}{p['pdf']}">PDF</a> · <a href="{LINK_BASE}{p['md']}">Markdown</a></p>
<details><summary>Read full paper</summary><div class="fulltext">{p['body_html']}</div></details>
</article>"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pages-dir", default=None,
                    help="Build the public GitHub Pages version into this dir "
                         "(index.html + papers-data.json + papers/ copies).")
    args = ap.parse_args()
    global LINK_BASE
    out_dir = HERE
    html_name = "site.html"
    if args.pages_dir:
        LINK_BASE = "papers/"
        out_dir = Path(args.pages_dir)
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "papers").mkdir(exist_ok=True)
        html_name = "index.html"
    papers = collect()
    counts = {t: sum(1 for p in papers if p["field"] == t) for t in FIELDS}
    total = len(papers)
    manifest = [{k: v for k, v in p.items() if k != "body_html"} | {"summary": summary_of(p["abstract"])} for p in papers]
    (out_dir / "papers-data.json").write_text(json.dumps(manifest, indent=1, ensure_ascii=False), encoding="utf-8")
    if args.pages_dir:
        for p in papers:
            for fname in (p["md"], p["pdf"]):
                src = FILES / fname
                if src.exists():
                    shutil.copy2(src, out_dir / "papers" / fname)
        print(f"copied {total} md + pdf pairs into {out_dir / 'papers'}")

    sections = []
    for field in FIELDS:
        group = [p for p in papers if p["field"] == field]
        if not group:
            continue
        group.sort(key=lambda p: p["date"], reverse=True)
        cards = "\n".join(card(p, i) for i, p in enumerate(group))
        sections.append(
            f'<section id="sec-{field}" data-field="{field}"><h2>{TRACK_LABEL[field]} <span class="count">({len(group)})</span></h2>\n{cards}\n</section>'
        )
    body = "\n".join(sections)
    page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>Research Papers — Zubair Ali</title>
<style>
*{{box-sizing:border-box}}
body{{font-family:system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;max-width:920px;margin:0 auto;padding:24px 16px;color:#1c1c1c;line-height:1.55}}
h1{{font-family:Georgia,serif;font-size:30px;margin:0 0 4px}}
h2{{font-family:Georgia,serif;border-bottom:2px solid #1c1c1c;padding-bottom:6px;margin-top:36px}}
.sub{{color:#555;margin:0 0 14px}}
.counts{{display:flex;gap:10px;flex-wrap:wrap;margin:14px 0}}
.counts b{{background:#f0ead9;border:1px solid #ddd;padding:8px 12px;border-radius:10px}}
.note{{background:#fdf6e3;border:1px solid #e8d9a0;padding:12px 14px;border-radius:10px;font-size:14px}}
.note b{{color:#7a5b00}}
.controls{{position:sticky;top:0;background:#fff;padding:10px 0;border-bottom:1px solid #e5e0d5;display:flex;gap:8px;flex-wrap:wrap;align-items:center;z-index:5}}
.controls input[type=search]{{flex:1;min-width:180px;padding:9px 12px;font-size:15px;border:1px solid #ccc;border-radius:8px}}
.controls button{{padding:9px 14px;font-size:14px;border:1px solid #ccc;background:#f7f5f0;border-radius:999px;cursor:pointer}}
.controls button.on{{background:#1c1c1c;color:#fff;border-color:#1c1c1c}}
.card{{border:1px solid #e5e0d5;border-radius:12px;padding:16px;margin:14px 0;background:#fff}}
.card h3{{font-family:Georgia,serif;font-size:19px;margin:8px 0}}
.meta{{font-size:13px;color:#666;display:flex;gap:8px;flex-wrap:wrap;align-items:center}}
.badge{{font-size:11px;font-weight:700;padding:2px 9px;border-radius:999px}}
.health{{background:#dcefe0}} .brain{{background:#dde8f7}} .space{{background:#efe3f7}}
.abs{{margin:8px 0}}
.links{{font-size:13px;margin:6px 0}}
a{{color:#0b5cad}}
details{{margin-top:10px;border-top:1px solid #eee;padding-top:10px}}
details summary{{cursor:pointer;font-weight:600;color:#0b5cad}}
.fulltext{{font-size:15px}}
.fulltext h2{{font-size:20px;border:none;margin:20px 0 8px}}
.fulltext h3{{font-size:17px;margin:16px 0 6px}}
.fulltext table{{border-collapse:collapse;width:100%;overflow-x:auto;display:block;font-size:13px}}
.fulltext th,.fulltext td{{border:1px solid #ddd;padding:6px 8px;text-align:left}}
.fulltext pre{{background:#f5f5f5;padding:10px;overflow-x:auto;font-size:13px}}
.fulltext img{{max-width:100%}}
.hidden{{display:none!important}}
footer{{color:#777;font-size:13px;margin-top:32px;border-top:1px solid #e5e0d5;padding-top:12px}}
</style>
</head>
<body>
<h1>Research Papers</h1>
<p class="sub">Zubair Ali — Pharm-D student, SMBBMU Larkana, Pakistan · ORCID 0009-0001-5921-7509 · <a href="https://github.com/zubair0153715/daily-health-papers">daily-health-papers on GitHub</a></p>
<div class="counts"><b>{total} manuscripts</b><b>Health: {counts['health']}</b><b>Brain: {counts['brain']}</b><b>Space: {counts['space']}</b><b>Natural Science: {counts['natural']}</b><b>Social Science: {counts['social']}</b><b>Drug Discovery: {counts['drugdiscovery']}</b></div>
<p class="note"><b>AI-assisted drafts — NOT peer-reviewed, NOT published.</b> All claims require independent verification. Two early manuscripts were submitted to ChemRxiv and rejected (framework/hypothesis without new data); their reworked v2 versions are marked "ready to submit". Nothing here is submitted anywhere — submission is the author's own click after he approves a paper. New manuscripts are added daily.</p>
<div class="controls">
<input type="search" id="q" placeholder="Search titles…" aria-label="Search papers"/>
<button data-f="all" class="on">All</button>
<button data-f="health">Health</button>
<button data-f="brain">Brain</button>
<button data-f="space">Space</button>
<button data-f="natural">Natural Science</button>
<button data-f="social">Social Science</button>
<button data-f="drugdiscovery">Drug Discovery</button>
</div>
{body}
<footer>Updated {date.today().strftime('%d %b %Y')} · Generated from the manuscripts in files/ by files/papers-website/build-site.py — re-run it after each daily papers run, then update the website. Author: Zubair Ali; drafting assistant: Lapis (AI).</footer>
<script>
const q=document.getElementById('q');
const btns=[...document.querySelectorAll('.controls button')];
let field='all';
function apply(){{
  const needle=q.value.trim().toLowerCase();
  document.querySelectorAll('.card').forEach(c=>{{
    const okF = field==='all' || c.dataset.field===field;
    const okQ = !needle || c.dataset.title.includes(needle) || c.querySelector('.abs').textContent.toLowerCase().includes(needle);
    c.classList.toggle('hidden', !(okF && okQ));
  }});
  document.querySelectorAll('section[data-field]').forEach(s=>{{
    const vis=[...s.querySelectorAll('.card')].some(c=>!c.classList.contains('hidden'));
    s.classList.toggle('hidden', !vis);
  }});
}}
q.addEventListener('input', apply);
btns.forEach(b=>b.addEventListener('click', ()=>{{field=b.dataset.f;btns.forEach(x=>x.classList.toggle('on',x===b));apply();}}));
</script>
</body>
</html>
"""
    (out_dir / html_name).write_text(page, encoding="utf-8")
    print(f"wrote {html_name} ({len(page)/1024:.0f} KB) + papers-data.json: {total} papers "
          f"(health {counts['health']}, brain {counts['brain']}, space {counts['space']})")


if __name__ == "__main__":
    main()
