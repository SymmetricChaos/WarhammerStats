import csv
from pathlib import Path
from Translators import tech_stat_translator

top_of_path = str(Path(__file__).parent)



# What effect value is tied to each key
key_to_effect_vals = {}
# What effect_keys are tied to each tech_key
tech_key_to_keys = {}
with open(top_of_path+'\\DataFiles\\technology_effects_junction_tables.tsv', encoding="utf8") as f:
    F = csv.reader(f,delimiter='\t')
    
    for n,row in enumerate(F):
        if n < 3:
            continue
        
        if row[1] in key_to_effect_vals:
            key_to_effect_vals[row[1]] += [row[3]]
        else:
            key_to_effect_vals[row[1]] = [row[3]]
            
        if row[0] in tech_key_to_keys:
            tech_key_to_keys[row[0]] += [row[1]]
        else:
            tech_key_to_keys[row[0]] = [row[1]]


#What tech_key corresponds to each name in the UI
tech_key_to_name = {}
with open(top_of_path+'\\DataFiles\\technologies__.loc.tsv', encoding="utf8") as f:
    F = csv.reader(f,delimiter='\t')
    
    for n,row in enumerate(F):
        try:
            tech_key,name,_ = row
            if "onscreen" in tech_key and name != "":
                tech_key_to_name[tech_key[27:]] = name
        except:
            if "onscreen" in row[0]:
                print(row)

# What units are in each unit set
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

# What unit sets are tied to each effect key
# What stat is tied to each effect key
key_to_unit_set = {}
key_to_stat = {}
with open(top_of_path+'\\DataFiles\\effect_bonus_value_ids_unit_sets_tables.tsv', encoding="utf8") as f:
    F = csv.reader(f,delimiter='\t')
    
    for n,row in enumerate(F):
        if n < 5:
            continue
        
        stat,key,unit_set = row
        
        if key in key_to_unit_set:
            if unit_set not in key_to_unit_set[key]:
                key_to_unit_set[key] += [unit_set]
        else:
            key_to_unit_set[key] = [unit_set]
        
        
        if key in key_to_stat:
            if stat not in key_to_stat[key]:
                key_to_stat[key] += [stat]
        else:
            key_to_stat[key] = [stat]


# What units are tied to each key
key_to_units = {}
for k,v in key_to_unit_set.items():
    key_to_units[k] = []
    for unit_set in v:
        try:
            key_to_units[k] += unit_set_to_units[unit_set]
        except:
            key_to_units[k] += ["ERROR"+unit_set]



# Tie everything to the name
name_to_info = {}
for tech_key,name in tech_key_to_name.items():
    if tech_key not in tech_key_to_keys:
        continue
    effect_keys = tech_key_to_keys[tech_key]
    effects = []
    for e in effect_keys:
        if e not in key_to_stat:
            continue

        for k in key_to_stat[e]:
            if k not in tech_stat_translator:
                continue
            stat_effects = tech_stat_translator[k]

            stat_value = key_to_effect_vals[e]
            effect_tuple = (stat_effects[0],stat_value[0],stat_effects[1])
            effects.append(effect_tuple)

    name_to_info[name] = effects

print(name_to_info['Marching Songs'])
