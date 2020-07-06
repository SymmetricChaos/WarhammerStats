import json
from ExploreJSON import show_dict
with open('fatigue.json', encoding="utf8") as f:
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
    


if __name__ == '__main__':
    show_dict(fatigue_dict)

