import json
from ExploreJSON import show_dict
with open('fatigue.json', encoding="utf8") as f:
    F = json.load(f)

fatigue_dict = {}
for level in F:
    subdict = {}
    subdict["speed"] = level["scalar_speed"]
    subdict["melee_attack"] = level["stat_melee_attack"]
    subdict["melee_defence"] = level["stat_melee_defence"]
    subdict["armour"] = level["stat_armour"]
    subdict["charge_bonus"] = level["stat_charge_bonus"]
    subdict["melee_ap_damage"] = level["stat_melee_damage_ap"]

    fatigue_dict[level["key"][10:]] = subdict
    
show_dict(fatigue_dict)