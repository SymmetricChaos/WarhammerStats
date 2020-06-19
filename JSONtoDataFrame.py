import json
import pandas as pd 
import pickle
from UtilityFunctions import no_nonstandard, deduplicate_lore

with open('unitsdata.json', encoding="utf8") as f:
  J = json.load(f)
  
# Make a somewhat cleaner object to that is easier to work with than the raw JSON data

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
    weapon = unit["primary_melee_weapon"]
    D["melee_base_damage"] = weapon["base_damage"]
    D["melee_ap_damage"] = weapon["ap_damage"]
    D["melee_total_damage"] = weapon["damage"]
    D["melee_ap_ratio"] = weapon["ap_ratio"]
    D["melee_bonus_v_large"] = weapon["bonus_v_large"]
    D["melee_bonus_v_infantry"] = weapon["bonus_v_infantry"]
    D["melee_attack_interval"] = weapon["melee_attack_interval"]
    D["melee_is_magical"] = weapon["is_magical"]
    D["melee_is_flaming"] = weapon["ignition_amount"] # <- renamed to reflect player facing name
    if weapon["phase"] == None:
        D["melee_contact_effect"] = ""
    else:
        D["melee_contact_effect"] = weapon["phase"]["name"].split("\\")[0] # <- contact effects can contain an image after the name
    

# Mutate some dictionary D to add the ranged vital stats of unit
def set_ranged_stats(D,unit):
    # Some units have no missile attack so we set them all those stats to None
    # (Pandas may actually take care of this automatically but we also want a
    #  raw dictionary output as an option and this will avoid key errors when
    #  iterating through it.)
    if unit["primary_missile_weapon"] == {}:
        D["ranged_base_damage"] = None
        D["ranged_ap_damage"] = None
        D["ranged_total_damage"] = None
        D["ranged_ap_ratio"] = None
        D["ranged_bonus_v_large"] = None
        D["ranged_bonus_v_infantry"] = None
        D["ranged_is_magical"] = None
        D["ranged_is_flaming"] = None
        D["ranged_contact_effect"] = ""
        D["ammo"] = None
        D["base_reload_time"] = None
        D["range"] = None
        D["shots_per_volley"] = None
        D["projectile_number"] = None
        D["calibration_area"] = None
        D["calibration_distance"] = None
        
        # If there is no ranged attack there is also no explosion so again we
        # provide default values
        D["explosion_base_damage"] = None
        D["explosion_ap_damage"] = None
        D["explosion_radius"] = None
        D["explosion_is_magical"] = None
        D["explosion_is_flaming"] = None
        D["explosion_contact_effect"] = ""


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
        D["ranged_is_magical"] = projectile["is_magical"]
        D["ranged_is_flaming"] = projectile["ignition_amount"]
        D["calibration_area"] = projectile["calibration_area"] # precision
        D["calibration_distance"] = projectile["calibration_distance"] # some modifier to precision
        if projectile["phase"] == None:
            D["ranged_contact_effect"] = ""
        else:
            D["ranged_contact_effect"] = projectile["phase"]["name"].split("\\")[0]
        
        # Some units have no explosion so those stats are set to None
        if projectile["explosion"] == None:
            D["explosion_base_damage"] = None
            D["explosion_ap_damage"] = None
            D["explosion_radius"] = None
            D["explosion_is_magical"] = None
            D["explosion_is_flaming"] = None
            D["explosion_contact_effect"] = ""
            
        else:
            D["explosion_base_damage"] = projectile["explosion"]["base_damage"]
            D["explosion_ap_damage"] = projectile["explosion"]["ap_damage"]
            D["explosion_radius"] = projectile["explosion"]["detonation_radius"]
            D["explosion_is_magical"] = projectile["explosion"]["is_magical"]
            D["explosion_is_flaming"] = projectile["explosion"]["ignition_amount"]
            if projectile["explosion"]["phase"] == None:
                D["explosion_contact_effect"] = ""
            else:
                D["explosion_contact_effect"] = projectile["explosion"]["phase"]["name"].split("\\")[0]
        
        # Need to validate meaning of ammo count
        # Used to be total volleys but now user interface shows total shots
        D["ammo"] = unit["primary_missile_weapon"]["ammo"]
        




units = []

for unit in J:
    if unit["name"] == "TEST UNIT - Tomb Kings" or unit["caste"] == "Generic":
        continue
    D = {# Simple user facing stats
         "name": unit["name"],
         "health": unit["health"],
         "leadership": unit["leadership"],
         "charge_bonus": unit["charge_bonus"],
         "armour": unit["armour"],
         "melee_attack": unit["melee_attack"],
         "melee_defence": unit["melee_defence"],
         "is_large": unit["is_large"], # <- controls the UI symbol for infantry or large size
         "missile_block_chance": unit["parry_chance"], # <- renamed to common name
         "unit_size": unit["unit_size"], # <- number of entities
         "damage_mod_flame": unit["damage_mod_flame"],
         "damage_mod_magic": unit["damage_mod_magic"],
         "damage_mod_physical": unit["damage_mod_physical"],
         "damage_mod_missile": unit["damage_mod_missile"],
         "damage_mod_all": unit["damage_mod_all"],
         "speed": unit["speed"], # <- speed as shown in UI, better of ground and flying
         "recruitment_time":  unit["create_time"], # <- recruitment time
         "unit_card":unit["unit_card"].split("/")[-1],
         
         
         # Simple non-user facing stats
         "health_per_entity": unit["health_per_entity"],
         
         "multiplayer_cost": unit["multiplayer_cost"],
         "singleplayer_cost":  unit["singleplayer_cost"],
         "singleplayer_upkeep":  unit["singleplayer_upkeep"],
         
         "mass": unit["mass"],
#         "weight": unit["weight"], # <- According to devs no longer used
         "height": unit["height"],
         "radius": unit["radius"],
         "entity_size": unit["entity_size"],
         
         "caste": unit["caste"],  
         "category": unit["category"],
         "special_category": unit["special_category"],

         "key": unit["key"],
         
         "speed_ground": unit["run_speed"],
         "speed_flying": unit["fly_speed"],
         "charge_speed": unit["charge_speed"],
         "charge_speed_flying": unit["flying_charge_speed"],
         
         "ground_stat_effect_group": unit["ground_stat_effect_group"]["group_name"],
         
         "reload_skill": unit["reload"],

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




# Convert to a pandas DataFrame
unitsDF = pd.DataFrame(units)
# Save as a DataFrame, as a dictionary, and as a csv file
pickle.dump(unitsDF, open( "unitsDF.p", "wb" ) )
pickle.dump(units, open( "unitsDict.p", "wb" ) )
unitsDF.to_csv("units.csv")


# Create a deeply cleaned version of the DataFrame that removed all non-standard
# units and turns characters that differ only in lore into a single entry
# This is often useful when looking at staistics of a whole faction
unitsDFclean = no_nonstandard(unitsDF)
unitsDFclean = deduplicate_lore(unitsDFclean)

pickle.dump(unitsDF, open( "unitsDF_clean.p", "wb" ) )
pickle.dump(units, open( "unitsDict_clean.p", "wb" ) )
unitsDF.to_csv("units_clean.csv")

