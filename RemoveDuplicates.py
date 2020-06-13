import numpy as np
import matplotlib.pyplot as plt
import pickle
from UtilityFunctions import all_from_faction, no_single_entity

units = pickle.load( open( "unitsDF.p", "rb" ) )

# All lores of magic that can be had by multiple identical units
# We will replace these with just ""
lores = [" (Beasts)",
         " (Death)",
         " (Fire)",
         " (Heavens)",
         " (High)",
         " (Life)",
         " (Light)",
         " (Metal)",
         " (Shadows)",
         " (Dark)",
         " (Vampires)",
         " (Deep)",
         " (Plague)",
         " (Ruin)"]

def remove_lore(name):
    for lore in lores:
        if lore in name:
            name = name.replace(lore," ")
            name = name.replace("  "," ")
            return name
    return name

# Warning! This list should not be used for names as there may be spacing issues
def deduplicate_lore(units):

    names = units["name"]
    reduced_names = []
    for name in names:
        reduced_names.append(remove_lore(name))
    
    units_no_dupe_lores = units.replace(list(units["name"]),reduced_names)
    units_no_dupe_lores.drop_duplicates(subset="name",inplace=True)
    
    return units_no_dupe_lores
        

if __name__ == '__main__':
    
    print("Many units are effectively duplicates of each other which may skew numbers when analysed.")
    print("For instance the High Elves have a total of 9 types of Mages and Archmages. Each of those has at least three mount options, including on foot. This large number of heroic units skews certains stats significantly.")
    hef = all_from_faction(units,"hef")
    grn = all_from_faction(units,"grn")
#    for name in hef['name']:
#        if "mage" in name.lower():
#            print(name)
    print("Consider that weapon damage for single entities (such as lords and heroes) is very very high.")
    print("If we look at the mean weapon damage for the high elves is incredibly high compared to a faction with few heroic units like the greenskins.")
    print(f"hef mean damage: {round(np.nanmean(hef['melee_total_damage']))}")
    print(f"grn mean damage: {round(np.nanmean(grn['melee_total_damage']))}")
    print(f"Removing single entities from the factions should tell a different story.")
    hef_no_single = no_single_entity(hef)
    grn_no_single = no_single_entity(grn)
    print(f"hef mean damage: {round(np.nanmean(hef_no_single['melee_total_damage']))}")
    print(f"grn mean damage: {round(np.nanmean(grn_no_single['melee_total_damage']))}")
    print("What was a difference of 50% is now a difference of 10%.")
    print("This issue can also be lessed by using the median here just more robust metrics in general.")
    print("However what would really be good would be to reduce all these duplicates to a single entry.")
    print("For example rather than Archmage (Death) on Great Eagle and Archmage (Fire) on Great Eagle and all the others it would be nice to just have Archmage on Great Eagle")
    
