import pickle
import pandas as pd
import numpy as np
from UtilityFunctions import random_unit, all_from_faction, all_attributes, \
                             all_abilities, all_spells, no_special_category, \
                             no_summoned

units = pickle.load( open( "unitsDF.p", "rb" ) )
pd.set_option('display.max_rows', 500)

brt = all_from_faction(units,'brt')
bst = all_from_faction(units,'bst')
chs = all_from_faction(units,'chs')
cst = all_from_faction(units,'cst')
dlf = all_from_faction(units,'def')
dwf = all_from_faction(units,'dwf')
emp = all_from_faction(units,'emp')
grn = all_from_faction(units,'grn')
hef = all_from_faction(units,'hef')
lzd = all_from_faction(units,'lzd')
nor = all_from_faction(units,'nor')
skv = all_from_faction(units,'skv')
tmb = all_from_faction(units,'tmb')
vmp = all_from_faction(units,'vmp')
wef = all_from_faction(units,'wef')


def show_categorical_stats():
    for cat in ['caste','category','entity_size','faction_group','entity_size',
                'ground_stat_effect_group','special_category',
                'melee_contact_effect','ranged_contact_effect',
                'explosion_contact_effect']:
        
        options = sorted(units[cat].unique())
        print(f"{cat}:\n{options}\n")
        



if __name__ == '__main__':


    print("Show A random Unit's Stats\n")
    R = random_unit(units)
    print(R)
#    print("\n\n\n\nShow the various categories a unit can fall into\n")
#    show_categorical_stats()
#    
#    print(units[units["reload_skill"]==15])

#    print(emp["key"])
    # Special Keys found: waaagh, summoned, final_battle, aquitaine, graktar,
    #    imperial_supply, nakai, blessed
#    print(unitsDF[unitsDF["key"].str.contains('aquitaine')])
#    print(all_from_faction(unitsDF,'cst')["key"])
    
#    print(all_attributes(unitsDF))
#    print(all_abilities(unitsDF))
#    print(all_spells(unitsDF))
#    print(wef[["name","key"]])