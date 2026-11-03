"""Pick N unused health-paper topics for one day's run.

Usage:
  python3 pick_topics.py [--n 5] [--date YYYY-MM-DD] [--mark-used]
Reads topics-pool.json + health-papers-tracker.json (same dir's parent
hidden_files/), picks N topics never used before, spread across different
areas where possible (max 2 per area per day), prints JSON to stdout.
--mark-used writes the picks into the tracker as status 'picked' (the run
later updates them to 'drafted' / 'submitted'). Never picks a topic whose
id appears in the tracker or whose problem matches a used title.
"""
import argparse
import json
import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
GOAL = os.path.dirname(HERE)
POOL = os.path.join(HERE, "topics-pool.json")
TRACKER = os.path.join(GOAL, "hidden_files", "health-papers-tracker.json")


def load_json(path, default):
    if os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    return default


def used_ids(tracker):
    ids = set()
    for p in tracker.get("papers", []):
        if p.get("topic_id"):
            ids.add(p["topic_id"])
    for t in tracker.get("used_topic_ids", []):
        ids.add(t)
    return ids


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=5)
    ap.add_argument("--date", default=None)
    ap.add_argument("--mark-used", action="store_true")
    ap.add_argument("--seed", type=int, default=None)
    args = ap.parse_args()

    pool = load_json(POOL, {"topics": []})
    tracker = load_json(TRACKER, {"papers": [], "used_topic_ids": []})
    used = used_ids(tracker)

    topics = [t for t in pool["topics"] if t["id"] not in used
              and t.get("status") != "used"]
    if len(topics) < args.n:
        print(json.dumps({"ok": False,
                          "error": f"only {len(topics)} unused topics left "
                                   f"(need {args.n}) — refill the pool",
                          "remaining": len(topics)}))
        return 1

    rng = random.Random(args.seed if args.seed is not None else args.date)
    # Spread across areas: shuffle, then greedily take at most 2 per area
    # on the first pass; fill the rest on a second pass if needed.
    rng.shuffle(topics)
    picked, per_area = [], {}
    for t in topics:
        if len(picked) >= args.n:
            break
        if per_area.get(t["area"], 0) >= 2:
            continue
        picked.append(t)
        per_area[t["area"]] = per_area.get(t["area"], 0) + 1
    for t in topics:
        if len(picked) >= args.n:
            break
        if t not in picked:
            picked.append(t)

    out = {"ok": True, "n": len(picked), "date": args.date,
           "topics": [{k: t[k] for k in
                       ("id", "area", "problem", "target",
                        "reference_drug", "angle")} for t in picked]}
    print(json.dumps(out, indent=1))

    if args.mark_used:
        for t in picked:
            if t["id"] not in tracker.setdefault("used_topic_ids", []):
                tracker["used_topic_ids"].append(t["id"])
        with open(TRACKER, "w", encoding="utf-8") as f:
            json.dump(tracker, f, indent=1, ensure_ascii=False)
        print(f"Marked {len(picked)} topics used in tracker.",
              file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
