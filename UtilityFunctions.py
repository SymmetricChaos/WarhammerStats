import numpy as np
import pickle
import pandas as pd
pd.set_option('display.max_rows', 50)
pd.set_option('display.max_columns', 60)
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
    Returns the average damage done by an attack with given total damage and 
    ap ratio against a target with given armor
    """
    ap_damage = total_damage*ap_ratio
    base_damage = total_damage-ap_damage
    return average_damage_with_armor_raw(base_damage,ap_damage,armor)

## Most functions below accept the argument "units" which should be a pandas
## DataFrame where each row is a unit description like the one created by
## JSONtoDataFrame

def random_unit(units):
    # randint returns a list, the comma just skips having to extract the only
    # element of the list
    r, = np.random.randint(0,1365,1)
    return units.iloc[r]



# Attributes, abilitiesm and spells are all stored as lists this extracts all
# the unique attributes, abilities, or spells in a given units dataframe
def all_attributes(units):
    attributes = set([])
    for unit_atts in units["attributes"]:
        for att in unit_atts:
            attributes.add(att)
    return sorted(attributes)
    
def all_abilities(units):
    abilities = set([])
    for unit_abs in units["abilities"]:
        for ab in unit_abs:
            abilities.add(ab)
    return sorted(abilities)

def all_spells(units):
    spells = set([])
    for unit_spells in units["spells"]:
        for spell in unit_spells:
            spells.add(spell)
    return sorted(spells)



# Version of a unitsDF that has no single entities
def no_single_entity(units):
    is_not_single_entity = units["unit_size"] != 1
    return units[is_not_single_entity]

# Version of a unitsDF that has no special units. Meaning these kinds are removed:
# 'blessed_spawning', 'crafted', 'elector_counts', 'mistwalker', 'renown', 'tech_lab'
def no_special_category(units):
    is_not_special_category = units["special_category"] == ""
    return units[is_not_special_category]

def all_with_ability(units,ability):
    has_ability = []
    print(units["abilities"])
    for L in units["abilities"]:
        if ability in L:
            has_ability.append(True)
        else:
            has_ability.append(False)
    return units[has_ability]

def all_with_attribute(units,attribute):
    has_attribute = []
    print(units["attributes"])
    for L in units["attributes"]:
        if attribute in L:
            has_attribute.append(True)
        else:
            has_attribute.append(False)
    return units[has_attribute]





if __name__ == '__main__':
    
#    print(100/average_damage_with_armor_ratio(100,.7,200))
    print(no_single_entity(unitsDF))
    
#    print(all_with_ability(unitsDF,"Foe-Seeker"))
    
#    print(all_with_attribute(unitsDF,"strider"))

    