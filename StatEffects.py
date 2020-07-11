import csv
from TWWObjects import TWWEffect
from Translators import stat_translator
from MakeEffectDict import ability_key_to_name

# The stat effects can be found in the:
# special_abilty_phase_stat_effects_tables
# Need to find a way to get correct names
name_and_effects = {}
with open("stat_effects_tables.tsv") as fd:
    rd = csv.reader(fd, delimiter="\t", quotechar='"')
    for n,row in enumerate(rd):
        if n < 3:
            continue
        key = "_".join(row[0].split("_")[4:]) # split off unwanted part of key
        try:
            pretty_name = ability_key_to_name[key]
            if pretty_name not in name_and_effects:
                name_and_effects[pretty_name] = [(float(row[1]),stat_translator[row[2]],row[3])]
            else:
                name_and_effects[pretty_name].append((float(row[1]),stat_translator[row[2]],row[3]))
        except:
            print(key,row[0])

# Same with raw names for everything
name_and_effects_raw = {}
with open("stat_effects_tables.tsv") as fd:
    rd = csv.reader(fd, delimiter="\t", quotechar='"')
    for n,row in enumerate(rd):
        if n < 3:
            continue
        if row[0] not in name_and_effects_raw:
            name_and_effects_raw[row[0]] = [(float(row[1]),row[2],row[3])]
        else:
            name_and_effects_raw[row[0]].append((float(row[1]),row[2],row[3]))

effects_dict = {}
for name,effects in name_and_effects.items():
    E = TWWEffect(name,effects)
    effects_dict[E.pretty_name] = E


if __name__ == '__main__':
    import json
    import pickle
    
    with open('stat_effects_raw.json', 'w') as fp:
        json.dump(name_and_effects_raw, fp)
    
    pickle.dump(effects_dict, open( "effectsDict.p", "wb" ) )