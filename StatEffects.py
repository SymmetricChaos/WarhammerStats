import json
import pickle
from TWWObjects import TWWEffect
from Translators import stat_translator, attribute_pretty_name

with open('TWWAbilities.json', encoding="utf8") as f:
    A = json.load(f)

effects_dict = {}
for ability in A:
    stat_effects = []
    other_effects = []
    
    try:
        stats = ability['sa_phase']['statEffects']
        for s in stats:
            stat_effects.append( (stat_translator[s['stat']], s['value'], s['how']) )
    except:
        pass
    
    try:
        attributes = ability['sa_phase']['attributeEffects']
        for attr in attributes:
            other_effects.append( attribute_pretty_name[attr['attribute']] )
    except:
        pass
    
    try:
        phase = ability['sa_phase']
        if phase["unbreakable"]:
            other_effects.append("unbreakable")
        if phase["imbue_magical"]:
            other_effects.append("imbue_magical")
        if phase["imbue_ignition"]:
            other_effects.append("imbue_ignition")
    except:
        pass
    
    E = TWWEffect(ability["name"],ability["key"],stat_effects,other_effects)
    # This has a minor issue due to some abilities have the same name
    if E.name in effects_dict:
        if str(E.stat_effects) != str(effects_dict[E.name].stat_effects) or \
           str(E.other_effects) != str(effects_dict[E.name].other_effects):
               print(f"CONFLICT {E.name}")
               oldstat = E.stat_effects
               oldother = E.other_effects
               print(f"old:\n{oldstat}\n{oldother}")
               newstat = effects_dict[E.name].stat_effects
               newother = effects_dict[E.name].other_effects
               print(f"new:\n{newstat}\n{newother}")
               keep = input("keep:...")
               if keep == "old":
                   pass
               if keep == "new":
                   continue
    effects_dict[E.name] = E
    
pickle.dump(effects_dict, open( "effectsDict.p", "wb" ) )
print(effects_dict["Regeneration"])
print(effects_dict["Regeneration"].stat_effects)
print(effects_dict["Regeneration"].other_effects)