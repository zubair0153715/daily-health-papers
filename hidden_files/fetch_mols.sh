#!/bin/bash
for m in CHEMBL425963 CHEMBL222922 CHEMBL375172 CHEMBL222866 CHEMBL122450 CHEMBL45136 CHEMBL295625 CHEMBL379856; do
  for attempt in 1 2 3; do
    out=$(curl -s --max-time 45 --retry 2 --retry-delay 5 "https://www.ebi.ac.uk/chembl/api/data/molecule/$m.json")
    if echo "$out" | python3 -c "import json,sys; d=json.load(sys.stdin); ms=d.get('molecule_structures') or {}; print('$m','|', d.get('pref_name'), '|', (ms.get('canonical_smiles') or '')[:130])" 2>/dev/null; then break; fi
    sleep 6
  done
  sleep 3
done
