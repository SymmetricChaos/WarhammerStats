import csv
from pathlib import Path

top_of_path = str(Path(__file__).parent)




key_to_effect = {}
with open(top_of_path+'\\DataFiles\\technology_effects_junction_tables.tsv', encoding="utf8") as f:
    F = csv.reader(f,delimiter='\t')
    
    for n,row in enumerate(F):
        if n < 3:
            continue
        key_to_effect[row[1]] = row


with open(top_of_path+'\\DataFiles\\technologies__.loc.tsv', encoding="utf8") as f:
    F = csv.reader(f,delimiter='\t')
    
    for n,row in enumerate(F):
        if "onscreen" in row[0] and row[1] != "":
            if row[0][27:] in key_to_effect:
                key_to_effect[row[0][27:]].append(row[1])

unit_set_to_units = {}
with open(top_of_path+'\\DataFiles\\unit_set_to_unit_junctions_tables.tsv', encoding="utf8") as f:
    F = csv.reader(f,delimiter='\t')
    
    for n,row in enumerate(F):
        if n < 3:
            continue
        if row[5] not in unit_set_to_units:
            unit_set_to_units[row[5]] = [row[4]]
        else:
            unit_set_to_units[row[5]] += [row[4]]


key_to_unit_set = {}
with open(top_of_path+'\\DataFiles\\effect_bonus_value_ids_unit_sets_tables.tsv', encoding="utf8") as f:
    F = csv.reader(f,delimiter='\t')
    
    for n,row in enumerate(F):
        if n < 2:
            continue
        if row[1] in key_to_unit_set:
            if row[2] not in key_to_unit_set[row[1]]:
                key_to_unit_set[row[1]] += [row[2]]
        else:
            key_to_unit_set[row[1]] = [row[2]]

print("key_to_effect")
for k,v in key_to_effect.items():
    if 'wh2_dlc11_effect_force_unit_stat_weapon_damage_deckhands_depthguards' in k:
        print(k,v)
        break

print("\nunit_set_to_units")
for k,v in unit_set_to_units.items():
    if 'wh2_dlc11_cst_depth_guard' in k:
        print(k,v)
        break

print("\nkey_to_unit_set")
for k,v in key_to_unit_set.items():
    if 'wh2_dlc11_effect_force_unit_stat_weapon_damage_deckhands_depthguards' in k:
        print(k,v)
        break