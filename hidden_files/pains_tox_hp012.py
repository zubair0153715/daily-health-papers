import json, sys
sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import chem as C
from app.discovery import tox as T
named = {
    "vaborbactam": "B1(C(CCC(O1)CC(=O)O)NC(=O)CC2=CC=CS2)O",
    "relebactam": "C1CC(N2CC1N(C2=O)OS(=O)(=O)O)C(=O)NC3CCNCC3",
    "taniborbactam": "B1(C(CC2=C(O1)C(=CC=C2)C(=O)O)NC(=O)CC3CCC(CC3)NCCN)O",
}
out = {}
for name, smi in named.items():
    p = C.pains(smi)
    tox = None
    try:
        tox = T.tox_panel(smi)
    except Exception as e:
        tox = {"error": str(e)[:120]}
    sim = None
    try:
        sim = C.similarity_to(smi, ["C1CC(N2CC1N(C2=O)OS(=O)(=O)O)C(=O)N"])
    except Exception as e:
        sim = str(e)[:100]
    out[name] = {"pains": p, "tox": tox, "tanimoto_vs_avibactam": sim}
    print(name, "| pains:", p, "| tox:", json.dumps(tox)[:220] if tox else None, "| sim_vs_avi:", sim, flush=True)
json.dump(out, open("pains-tox-HP-012-named-2026-11-08.json", "w"), indent=1)
print("SAVED")
