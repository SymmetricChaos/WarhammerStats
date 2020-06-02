import json
import pandas as pd 
import pickle

with open('unitsdata.json', encoding="utf8") as f:
  J = json.load(f)
  
# Make a somewhat cleaner object to store
# We can expand later if we want

# Ultimately want to include at least these but use internal names
#  'class'
#  'BVL','BVI','damage','ap_damage','total_damage','ap_fraction',
#  'attack_interval','weight_class','melee_weapon',
#  'missile_weapon',,'missile_damage','missile_ap_damage',
#  'missile_total_damage','missile_projectiles','missile_shots_per_volley',
#  'ground_speed','fly_speed','missile_ap_fraction',
#  'missile_range','damage_mod_fire','damage_mod_magic',
#  'damage_mod_physical','damage_mod_missiles','damage_mod_all'

def get_attributes(D):
    att = D["attributes"]
    return [line["key"] for line in att]

def get_abilities(D):
    att = D["abilities"]
    return [line["name"] for line in att]

def get_factions(D):
    fac = D["factions"]
    return [line["screen_name"] for line in fac]

def get_faction_group(D):
    return D["key"].split("_")[2]

def get_spells(D):
    spl = D["spells"]
    return [line["name"] for line in spl]

# Mutate some dictionary D to add the melee vital stats of unit
def set_melee_stats(D,unit):
    D["melee_base_damage"] = unit["primary_melee_weapon"]["base_damage"],
    D["melee_ap_damage"] = unit["primary_melee_weapon"]["ap_damage"],
    D["melee_total_damage"] = unit["primary_melee_weapon"]["damage"],
    D["melee_ap_ratio"] = unit["primary_melee_weapon"]["ap_ratio"],
    D["melee_bonus_v_large"] = unit["primary_melee_weapon"]["bonus_v_large"],
    D["melee_bonus_v_infantry"] = unit["primary_melee_weapon"]["bonus_v_infantry"]

# Mutate some dictionary D to add the ranged vital stats of unit
def set_ranged_stats(D,unit):
    # Some units have no missile attack
    if unit["primary_missile_weapon"] == {}:
        D["ranged_base_damage"] = None
        D["ranged_ap_damage"] = None
        D["ranged_total_damage"] = None
        D["ranged_ap_ratio"] = None
        D["ranged_bonus_v_large"] = None
        D["ranged_bonus_v_infantry"] = None
        D["ammo"] = None
        D["base_reload_time"] = None
        D["range"] = None
        D["shots_per_volley"] = None
        D["projectile_number"] = None
    else:
        # Most ranged weapon stats are tied to the projectile
        projectile = unit["primary_missile_weapon"]["projectile"]
        
        D["ranged_base_damage"] = projectile["base_damage"]
        D["ranged_ap_damage"] = projectile["ap_damage"]
        D["ranged_total_damage"] = projectile["base_damage"]+projectile["ap_damage"]
        D["ranged_ap_ratio"] = projectile["ap_ratio"]
        D["ranged_bonus_v_large"] = projectile["bonus_v_large"]
        D["ranged_bonus_v_infantry"] = projectile["bonus_v_infantry"]
        D["base_reload_time"] = projectile["base_reload_time"]
        D["range"] = projectile["range"]
        D["shots_per_volley"] = projectile["shots_per_volley"]
        D["projectile_number"] = projectile["projectile_number"]
        
        # Some units have no explosion
        if projectile["explosion"] == None:
            D["explosion_base_damage"] = None
            D["explosion_ap_damage"] = None
            D["explosion_radius"] = None
        else:
            D["explosion_base_damage"] = projectile["explosion"]["base_damage"]
            D["explosion_ap_damage"] = projectile["explosion"]["ap_damage"]
            D["explosion_radius"] = projectile["explosion"]["detonation_radius"]
        
        # Need to validate meaning of ammo count
        # Used to be total volleys but now user interface shows total shots
        D["ammo"] = unit["primary_missile_weapon"]["ammo"]
        



units = []

for unit in J:
    D = {# Simple user facing stats
         "name": unit["name"],
         "health": unit["health"],
         "leadership": unit["leadership"],
         "charge_bonus": unit["charge_bonus"],
         "armour": unit["armour"],
         "melee_attack": unit["melee_attack"],
         "melee_defence": unit["melee_defence"],
         "entity_size": unit["entity_size"],
         "parry_chance": unit["parry_chance"],
         "unit_size": unit["unit_size"],
         "damage_mod_flame": unit["damage_mod_flame"],
         "damage_mod_magic": unit["damage_mod_magic"],
         "damage_mod_physical": unit["damage_mod_physical"],
         "damage_mod_missile": unit["damage_mod_missile"],
         "damage_mod_all": unit["damage_mod_all"],
         
         # Simple non-user facing stats
         "health_per_entity": unit["health_per_entity"],
         "multiplayer_cost": unit["multiplayer_cost"],
         "mass": unit["mass"],
         "caste": unit["caste"],
         "category": unit["category"],
         "special_category": unit["special_category"],
         "height": unit["height"],
         "radius": unit["radius"],
         "key": unit["key"],

         #Complex stats
         "factions": get_factions(unit),
         "faction_group": get_faction_group(unit),
         "attributes": get_attributes(unit),
         "abilities": get_abilities(unit),
         "spells": get_spells(unit)
         }
    
    # Weapon stats
    set_melee_stats(D,unit)
    set_ranged_stats(D,unit)

    units.append(D)

unitsDF = pd.DataFrame(units)
pickle.dump(unitsDF, open( "unitsDF.p", "wb" ) )
pickle.dump(units, open( "unitsDict.p", "wb" ) )
unitsDF.to_csv("units.csv")