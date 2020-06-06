import pickle
import pandas as pd
import numpy as np
from UtilityFunctions import random_unit, all_from_faction, all_attributes, \
                             all_abilities, all_spells

unitsDF = pickle.load( open( "unitsDF.p", "rb" ) )
pd.set_option('display.max_rows', 500)


def show_categorical_stats():
    for cat in ['caste','category','entity_size','faction_group','entity_size',
                'ground_stat_effect_group','special_category',
                'melee_contact_effect','ranged_contact_effect',
                'explosion_contact_effect']:
        
        options = sorted(unitsDF[cat].unique())
        print(f"{cat}:\n{options}\n")
        



if __name__ == '__main__':


#    print("Show A random Unit's Stats\n")
#    R = random_unit(unitsDF)
#    print(R)
    print("\n\n\n\nShow the various categories a unit can fall into\n")
    show_categorical_stats()
    

    
    # Special Keys found: waaagh, summoned, final_battle, aquitaine, graktar,
    #    imperial_supply, nakai, blessed
#    print(unitsDF[unitsDF["key"].str.contains('aquitaine')])
#    print(all_from_faction(unitsDF,'cst')["key"])
    
#    print(all_attributes(unitsDF))
#    print(all_abilities(unitsDF))
#    print(all_spells(unitsDF))
#    print(unitsDF[unitsDF["special_category"].str.contains('elector')])