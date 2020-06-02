import numpy as np

# I believe this is correct based on the description by the developers
# "Armour = Max damage reduction percentage. Min is always 50% of armour value.
#  To be more precise, any time base damage is dealt, the target rolls for 
#  armour. This armour roll is a random value between 50% and 100% of the 
#  armour stat. The armour roll is then applied as percentage damage 
#  reduction."
def armor_reduction(i):
    """Returns the percentage of base damage blocked by an armor value of i"""
    ar = np.linspace(i/2,i)
    ar = [min(x,100) for x in ar]
    return np.mean(ar)