import json, sys
sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import tox as T
named = {
    "vaborbactam": "B1(C(CCC(O1)CC(=O)O)NC(=O)CC2=CC=CS2)O",
    "relebactam": "C1CC(N2CC1N(C2=O)OS(=O)(=O)O)C(=O)NC3CCNCC3",
    "taniborbactam": "B1(C(CC2=C(O1)C(=CC=C2)C(=O)O)NC(=O)CC3CCC(CC3)NCCN)O",
}
out = {}
for name, smi in named.items():
    try:
        r = T.predict(smi)
    except Exception as e:
        r = {"error": str(e)[:200]}
    out[name] = r
    print(name, "|", json.dumps(r)[:400], flush=True)
json.dump(out, open("tox-HP-012-named-2026-11-08.json", "w"), indent=1)
print("SAVED")
