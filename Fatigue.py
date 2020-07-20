import json
import os

cur_dir = os.getcwd()
with open(cur_dir+'\\DataFiles\\twwstats_fatigue.json', encoding="utf8") as f:
    F = json.load(f)

# All of the effects of fatigue are multiplers so values of None are 
# equivalent to 1
none_to_one = lambda x: 1 if x == None else x

fatigue_dict = {}

fatigue_dict["fresh"] = {"threshold": 0,
                          "speed": 1,
                          "melee_attack": 1,
                          "melee_defence": 1,
                          "armour": 1,
                          "charge_bonus": 1,
                          "melee_ap_damage": 1}

for level in F:
    subdict = {}
    subdict["threshold"] = level["fatigue_threshold"]
    subdict["speed"] = none_to_one(level["scalar_speed"])
    subdict["melee_attack"] = none_to_one(level["stat_melee_attack"])
    subdict["melee_defence"] = none_to_one(level["stat_melee_defence"])
    subdict["armour"] = none_to_one(level["stat_armour"])
    subdict["charge_bonus"] = none_to_one(level["stat_charge_bonus"])
    subdict["melee_ap_damage"] = none_to_one(level["stat_melee_damage_ap"])

    fatigue_dict[level["key"][10:]] = subdict

fatigue_dict["animated"] = fatigue_dict["fresh"]
fatigue_dict["fading"] = fatigue_dict["winded"]
fatigue_dict["diminished"] = fatigue_dict["tired"]
fatigue_dict["debilitated"] = fatigue_dict["exhausted"]



import csv
import pickle

pickle.dump(fatigue_dict, open( "fatigueDict.p", "wb" ) )

with open(cur_dir+'\\DataFiles\\fatigue.csv', 'w') as f:
    w = csv.DictWriter(f, fatigue_dict.keys())
    w.writeheader()
    w.writerow(fatigue_dict)

with open(cur_dir+'\\DataFiles\\fatigue.json', 'w') as fp:
    json.dump(fatigue_dict, fp)