"""Validate a paper manuscript and extract its ChemRxiv submission-pack entry.

Usage:
  python3 make_pack.py <paper.md> [--date YYYY-MM-DD] [--append pack.md]
Extracts title (first # line), abstract (## Abstract section), keywords
(**Keywords:** line), checks ChemRxiv limits, prints a JSON entry.
  - abstract: plain text, max 2500 chars (fails loudly if over)
  - keywords: 3-10, each 3-50 chars
  - title: non-empty
With --append, adds a markdown section to the day's submission-pack file.
Exit 1 on any limit violation — a paper is only 'done' when its pack entry
validates.
"""
import argparse
import json
import re
import sys


def extract(md_text):
    lines = md_text.splitlines()
    title = next((l[2:].strip() for l in lines if l.startswith("# ")), "")
    m = re.search(r"## Abstract\n\n(.+?)\n\n---", md_text, re.S)
    if not m:
        m = re.search(r"## Abstract\n\n(.+?)\n\n## ", md_text, re.S)
    abstract = m.group(1).strip() if m else ""
    abstract_plain = abstract.replace("**", "").replace("*", "")
    abstract_plain = re.sub(r"\s+", " ", abstract_plain).strip()
    km = re.search(r"\*\*Keywords:\*\*\s*(.+)", md_text)
    keywords = []
    if km:
        keywords = [k.strip() for k in km.group(1).split(";")]
        keywords = [k for k in keywords if k]
    return title, abstract_plain, keywords


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("paper")
    ap.add_argument("--date", default=None)
    ap.add_argument("--append", default=None)
    args = ap.parse_args()

    text = open(args.paper, encoding="utf-8").read()
    title, abstract, keywords = extract(text)
    errors = []
    if not title:
        errors.append("missing title (# line)")
    if not abstract:
        errors.append("missing ## Abstract section")
    if len(abstract) > 2500:
        errors.append(f"abstract {len(abstract)} chars > 2500 limit")
    if not (3 <= len(keywords) <= 10):
        errors.append(f"{len(keywords)} keywords (need 3-10)")
    for k in keywords:
        if not (3 <= len(k) <= 50):
            errors.append(f"keyword out of 3-50 chars: {k!r}")

    entry = {"ok": not errors, "errors": errors, "title": title,
             "abstract_chars": len(abstract), "abstract": abstract,
             "keywords": keywords, "keyword_count": len(keywords),
             "subject_area": "Medicinal Chemistry / Chemical Biology",
             "licence": "CC BY 4.0",
             "author": "Zubair Ali", "orcid": "0009-0001-5921-7509",
             "affiliation": "SMBBMU, Larkana, Pakistan",
             "email": "za0153715@gmail.com"}
    print(json.dumps(entry, indent=1, ensure_ascii=False))

    if args.append and not errors:
        section = (
            f"\n## {title}\n\n"
            f"- **File:** `{args.paper.split('/')[-1]}`\n"
            f"- **Abstract:** {len(abstract)} characters (limit 2,500)\n"
            f"- **Keywords ({len(keywords)}):** {'; '.join(keywords)}\n"
            f"- **Subject area:** Medicinal Chemistry / Chemical Biology\n"
            f"- **Licence:** CC BY 4.0 · **Author:** Zubair Ali, "
            f"ORCID 0009-0001-5921-7509 · **Affiliation:** "
            f"SMBBMU, Larkana, Pakistan\n"
        )
        with open(args.append, "a", encoding="utf-8") as f:
            f.write(section)
        print(f"Appended pack entry to {args.append}", file=sys.stderr)
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
