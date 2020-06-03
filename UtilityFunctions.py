import numpy as np
import pickle
import pandas as pd
pd.set_option('display.max_rows', 50)
unitsDF = pickle.load( open( "unitsDF.p", "rb" ) )

# I believe this is correct based on the description by the developers
# "Armour = Max damage reduction percentage. Min is always 50% of armour value.
#  To be more precise, any time base damage is dealt, the target rolls for 
#  armour. This armour roll is a random value between 50% and 100% of the 
#  armour stat. The armour roll is then applied as percentage damage 
#  reduction."
def average_armor_reduction(armor):
    """Returns the proportion of base damage blocked by the given armor value"""
    ar = np.linspace(armor/2,armor)
    ar = [min(x,100) for x in ar]
    return np.mean(ar)/100

def average_damage_with_armor_raw(base_damage,ap_damage,armor):
    """
    Returns the average damage done by an attack with given base and ap damage
    against a target with given armor
    """
    armor_reduction = average_armor_reduction(armor)
    adjusted_base_damage = (1-armor_reduction)*base_damage
    return adjusted_base_damage+ap_damage

def average_damage_with_armor_ratio(total_damage,ap_ratio,armor):
    """
    Returns the average damage done by an attack with given base and ap damage
    against a target with given armor
    """
    ap_damage = total_damage*ap_ratio
    base_damage = total_damage-ap_damage
    return average_damage_with_armor_raw(base_damage,ap_damage,armor)

# Version of a unitsDF that has no single entities
def no_single_entity(units):
    is_not_single_entity = units["unit_size"] != 1
    return unitsDF[is_not_single_entity]

# Version of a unitsDF that has no special units. Meaning these kinds are removed:
# 'blessed_spawning', 'crafted', 'elector_counts', 'mistwalker', 'renown', 'tech_lab'
def no_special_category(units):
    is_not_special_category = units["special_category"] == ""
    return unitsDF[is_not_special_category]



if __name__ == '__main__':
    
    print(100/average_damage_with_armor_ratio(100,.7,200))
    print(no_single_entity(unitsDF))
    print(no_special_category(unitsDF))