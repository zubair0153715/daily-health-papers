#!/bin/bash
# Sequential manual docking for today's 5 topics (one Vina at a time:
# 6 parallel Vinas thrashed the 1.5-CPU VM). manual_dock.py saves
# incrementally and resumes, so a service restart loses at most one ligand.
cd "$(dirname "$0")"
export NO_PROXY=localhost,127.0.0.1,::1
PY=~/workspace/.venv-fc/bin/python
$PY manual_dock.py spec-HP-137-4ZUD.json dock-HP-137-2026-11-26-4ZUD.json > dock-HP-137-2026-11-26-4ZUD.log 2>&1; echo "137 EXIT:$?" >> dock-HP-137-2026-11-26-4ZUD.log
$PY manual_dock.py spec-HP-131-4LL3.json dock-HP-131-2026-11-26-4LL3.json > dock-HP-131-2026-11-26-4LL3.log 2>&1; echo "131-4LL3 EXIT:$?" >> dock-HP-131-2026-11-26-4LL3.log
$PY manual_dock.py spec-HP-131-6DH6.json dock-HP-131-2026-11-26-6DH6.json > dock-HP-131-2026-11-26-6DH6.log 2>&1; echo "131-6DH6 EXIT:$?" >> dock-HP-131-2026-11-26-6DH6.log
$PY manual_dock.py spec-HP-130-5EW8.json dock-HP-130-2026-11-26-5EW8.json > dock-HP-130-2026-11-26-5EW8.log 2>&1; echo "130 EXIT:$?" >> dock-HP-130-2026-11-26-5EW8.log
$PY manual_dock.py spec-HP-105-4ZYO.json dock-HP-105-2026-11-26-4ZYO.json > dock-HP-105-2026-11-26-4ZYO.log 2>&1; echo "105 EXIT:$?" >> dock-HP-105-2026-11-26-4ZYO.log
echo "ALL DOCKS DONE $(date -u +%H:%M)" >> dock-run-2026-11-26.log
