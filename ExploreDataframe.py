import pickle
import pandas as pd
import numpy as np
from UtilityFunctions import random_unit

unitsDF = pickle.load( open( "unitsDF.p", "rb" ) )
pd.set_option('display.max_rows', 500)


def show_categorical_stats():
    for cat in ['caste','category','entity_size','faction_group','entity_size',
                'ground_stat_effect_group','special_category']:
        
        options = sorted(unitsDF[cat].unique())
        print(f"{cat}:\n{options}\n")
        



if __name__ == '__main__':

    
#    print(unitsDF.iloc[0]['melee_attack'])
#    print("Show A random Unit's Stats\n")
#    random_unit()
#    print("\n\n\n\nShow the various categories a unit can fall into\n")
#    show_categorical_stats()
#    random_unit(unitsDF)
    
    print(np.nanmedian(unitsDF["melee_ap_ratio"]))