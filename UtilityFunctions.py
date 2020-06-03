import numpy as np

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





if __name__ == '__main__':
    
    print(100/average_damage_with_armor_ratio(100,.7,200))