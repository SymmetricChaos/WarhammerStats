import json
import pickle
from TWWObjects import TWWEffect
from Translators import stat_translator, attribute_pretty_name
import os

cur_dir = os.getcwd()

with open(cur_dir+'\\RawFiles\\TWWAbilities.json', encoding="utf8") as f:
    A = json.load(f)
with open(cur_dir+'\\RawFiles\\unitsdata.json', encoding="utf8") as f:
    U = json.load(f)


## Helper functions ##

def statEffects_to_list(statEffects):
    stat_effects_list = []
    for s in statEffects:
        stat_effects_list.append( (stat_translator[s['stat']], s['value'], s['how']) )
    return stat_effects_list

def handle_conflict(D,new_entry):
    if new_entry.name in D:
        if new_entry.display() != effects_dict[new_entry.name].display():
            print("\nCONFLICT")
            print("old")
            print(effects_dict[new_entry.name].display())
            print("\nnew")
            print(new_entry.display())
            rename = input("annotate which?")
            if rename == "old":
                newname = name + input("annotate old with:")
                D[newname] = D[name]
                D[newname] = newname
            if rename == "new":
                new_entry.name += input("annotate new with:")
    D[new_entry.name] = new_entry





effects_dict = {}
for ability in A:
    if 'sa_vortex_phase' in ability:
        if ability['sa_vortex_phase'] != None:
            
            phase = ability['sa_vortex_phase']
            name = phase['name']
            # All multiuse contact effects seems to have '!' in them
            if "!" not in name:
                name = ability['name']
            
            stat_effects = statEffects_to_list(phase['statEffects'])
            
            other_effects = []
            attributes = phase['attributeEffects']
            for attr in attributes:
                other_effects.append( attribute_pretty_name[attr['attribute']] )
            
            if phase["unbreakable"]:
                other_effects.append("unbreakable")
            if phase["imbue_magical"]:
                other_effects.append("imbue_magical")
            if phase["imbue_ignition"]:
                other_effects.append("imbue_flaming")
                
            E = TWWEffect(name,stat_effects,other_effects)
            handle_conflict(effects_dict,E)


for ability in A:
    stat_effects = []
    other_effects = []
    name = ability["name"]
    
    if 'sa_phase' not in ability or ability['sa_phase'] == None:
        continue
    
    sa_phase = ability['sa_phase']
    
    if 'statEffects' in sa_phase:
        stat_effects = statEffects_to_list(sa_phase['statEffects'])
    
    if 'attributeEffects' in sa_phase:
        attributes = sa_phase['attributeEffects']
        for attr in attributes:
            other_effects.append( attribute_pretty_name[attr['attribute']] )
    
    if sa_phase["unbreakable"]:
        other_effects.append("unbreakable")
    if sa_phase["imbue_magical"]:
        other_effects.append("imbue_magical")
    if sa_phase["imbue_ignition"]:
        other_effects.append("imbue_flaming")
    
    E = TWWEffect(name,stat_effects,other_effects)
    handle_conflict(effects_dict,E)





for unit in U:
    if 'primary_missile_weapon' in unit and unit['primary_missile_weapon'] != None:
        if 'phase' in unit['primary_missile_weapon'] and  unit['primary_missile_weapon']['phase'] != None:
            
            stat_effects = []
            other_effects = []
            name = unit['primary_missile_weapon']['phase']['name']
            
            if 'statEffects' in unit['primary_missile_weapon']['phase']:
                stat_effects = statEffects_to_list(unit['primary_missile_weapon']['phase']['statEffects'])
            
            if 'attributeEffects' in unit['primary_missile_weapon']['phase']:
                attributes = unit['primary_missile_weapon']['phase']['attributeEffects']
                for attr in attributes:
                    other_effects.append( attribute_pretty_name[attr['attribute']] )
            
            E = TWWEffect(name,stat_effects,other_effects)
            handle_conflict(effects_dict,E)


for unit in U:
    if 'phase' in unit['primary_melee_weapon'] and  unit['primary_melee_weapon']['phase'] != None:
            
        stat_effects = []
        other_effects = []
        name = unit['primary_melee_weapon']['phase']['name']
        
        if 'statEffects' in unit['primary_melee_weapon']['phase']:
            stat_effects = statEffects_to_list(unit['primary_melee_weapon']['phase']['statEffects'])
        
        if 'attributeEffects' in unit['primary_melee_weapon']['phase']:
            attributes = unit['primary_melee_weapon']['phase']['attributeEffects']
            for attr in attributes:
                other_effects.append( attribute_pretty_name[attr['attribute']] )
        
        E = TWWEffect(name,stat_effects,other_effects)
        handle_conflict(effects_dict,E)

pickle.dump(effects_dict, open(cur_dir+"\\WorkedFiles\\effectsDict.p", "wb" ) )
