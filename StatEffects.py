import json
import pickle
from TWWObjects import TWWEffect
from Translators import stat_translator, attribute_pretty_name

with open('TWWAbilities.json', encoding="utf8") as f:
    A = json.load(f)

effects_dict = {}
for ability in A:
    if 'bound' in ability['key']:
        continue
    if 'sa_vortex_phase' in ability:
        if ability['sa_vortex_phase'] != None:
            
            phase = ability['sa_vortex_phase']
            name = phase['name']
            # All multiuse contact effects seems to have '!' in them
            if "!" not in name:
                name = ability['name']
            
            stat_effects = []
            for s in phase['statEffects']:
                stat_effects.append( (stat_translator[s['stat']], s['value'], s['how']) )
            
            other_effects = []
            attributes = phase['attributeEffects']
            for attr in attributes:
                other_effects.append( attribute_pretty_name[attr['attribute']] )
            
            if phase["unbreakable"]:
                other_effects.append("unbreakable")
            if phase["imbue_magical"]:
                other_effects.append("imbue_magical")
            if phase["imbue_ignition"]:
                other_effects.append("imbue_ignition")
                
            E = TWWEffect(name,stat_effects,other_effects)
            if name in effects_dict and E.display() != effects_dict[name].display():
                print("CONFLICT")
                print(E.display())
                print(effects_dict[name].display())
                
            effects_dict[name] = E

for ability in A:
    if 'bound' in ability['key']:
        continue
    stat_effects = []
    other_effects = []
    name = ability["name"]
    
    if 'sa_phase' not in ability or ability['sa_phase'] == None:
        continue
    
    sa_phase = ability['sa_phase']
    
    if 'statEffects' in sa_phase:
        stats = sa_phase['statEffects']
        for s in stats:
            stat_effects.append( (stat_translator[s['stat']], s['value'], s['how']) )
    
    if 'attributeEffects' in sa_phase:
        attributes = sa_phase['attributeEffects']
        for attr in attributes:
            other_effects.append( attribute_pretty_name[attr['attribute']] )
        
    if sa_phase["unbreakable"]:
        other_effects.append("unbreakable")
    if sa_phase["imbue_magical"]:
        other_effects.append("imbue_magical")
    if sa_phase["imbue_ignition"]:
        other_effects.append("imbue_ignition")
    
    
    E = TWWEffect(name,stat_effects,other_effects)
    # This has a minor issue due to some abilities have the same name
    if name in effects_dict:
        if E.display() != effects_dict[name].display():
            print("CONFLICT")
            print("old")
            print(effects_dict[name].display())
            print("new")
            print(E.display())
            rename = input("rename which?")
            if rename == "old":
                newname = name + input("rename old to:")
                
                effects_dict[newname] = effects_dict[name]
                effects_dict[newname] = newname
            if rename == "new":
                E.name += input("rename new to:")
    effects_dict[E.name] = E

pickle.dump(effects_dict, open( "effectsDict.p", "wb" ) )
