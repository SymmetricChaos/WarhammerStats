import csv
from pathlib import Path

top_of_path = str(Path(__file__).parent)




key_to_effect = {}
with open(top_of_path+'\\DataFiles\\technology_effects_junction_tables.tsv', encoding="utf8") as f:
    F = csv.reader(f,delimiter='\t')
    
    for row in F:
        key_to_effect[row[0]] = row[1:]


with open(top_of_path+'\\DataFiles\\technologies__.loc.tsv', encoding="utf8") as f:
    F = csv.reader(f,delimiter='\t')
    
    for row in F:
        if "onscreen" in row[0] and row[1] != "":
            if row[0][27:] in key_to_effect:
                key_to_effect[row[0][27:]].append(row[1])


# with open(top_of_path+'\\DataFiles\\effect_bonus_value_ids_unit_sets_tables.tsv', encoding="utf8") as f:
#     F = csv.reader(f,delimiter='\t')
    
#     for row in F:
#         print(row)

unit_set_to_units = {}
with open(top_of_path+'\\DataFiles\\unit_set_to_unit_junctions_tables.tsv', encoding="utf8") as f:
    F = csv.reader(f,delimiter='\t')
    
    for n,row in enumerate(F):
        if n < 2:
            continue
        if row[5] not in unit_set_to_units:
            unit_set_to_units[row[5]] = [row[4]]
        else:
            unit_set_to_units[row[5]] += [row[4]]
            
for k,v in unit_set_to_units.items():
    print(k,v)