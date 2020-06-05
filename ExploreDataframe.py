import pickle
import pandas as pd
import numpy as np
from UtilityFunctions import random_unit

unitsDF = pickle.load( open( "unitsDF.p", "rb" ) )
pd.set_option('display.max_rows', 500)


def show_categorical_stats():
    for cat in ['caste','category','entity_size','faction_group','entity_size',
                'ground_stat_effect_group','special_category',
                'melee_contact_effect','ranged_contact_effect']:
        
        options = sorted(unitsDF[cat].unique())
        print(f"{cat}:\n{options}\n")
        



if __name__ == '__main__':


#    print("Show A random Unit's Stats\n")
#    print(random_unit(unitsDF))
    print("\n\n\n\nShow the various categories a unit can fall into\n")
    show_categorical_stats()
    random_unit(unitsDF)
    
#    print(np.nanmedian(unitsDF["melee_ap_ratio"]))