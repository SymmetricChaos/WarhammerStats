import numpy as np
import pickle
import pandas as pd
from UtilityFunctions import no_nonstandard, average_damage_with_armor_raw

unitsDF = pickle.load( open( "unitsDF.p", "rb" ) )
unitsDF = no_nonstandard(unitsDF)


def ranged_damage_stats(name,check_hawkish=True):
    unit = unitsDF[unitsDF["name"] == name]
    
    abilities = unit["abilities"].values[0]
                
    if check_hawkish:
    
        hawkish = "Hawkish Precision" in abilities
        
        if hawkish:
            ap_d = unit["ranged_ap_damage"].values[0]*1.15
        else:
            ap_d = unit["ranged_ap_damage"].values[0]
    else:
        hawkish = False
        ap_d = unit["ranged_ap_damage"].values[0]    
    
    
    base_d = unit["ranged_base_damage"].values[0]

    num_models = unit["unit_size"].values[0]
    num_proj = unit["projectile_number"].values[0]
    shot_vol = unit["shots_per_volley"].values[0]
    reload_time = unit["base_reload_time"].values[0]
    ammo = unit["ammo"].values[0]
    proj_range = unit["range"].values[0]
    speed = unit["speed"].values[0]
    
    damage_v_60a = average_damage_with_armor_raw(base_d,ap_d,60)

    damage_per_volley_60a = damage_v_60a*num_models*num_proj*shot_vol
    damage_per_second_60a = damage_per_volley_60a*(10/reload_time)
    damage_per_battle_60a = damage_per_volley_60a*ammo
    
    
    print(f"Some Ranged Damage Stats for {name}")
    
    if hawkish:
        print("Including Hawkish Precision")
    
    print("\nShooting at 60 Armor")
    print(f"Damage Per Projectile: {int(damage_v_60a)}")
    print(f"Damage Per Volley: {int(damage_per_volley_60a)}")
    print(f"Damage Per 10s: {int(damage_per_second_60a)}")
    print(f"Damage Per Battle: {int(damage_per_battle_60a)}")
    
    print(f"\nRange: {int(proj_range)}")
    print(f"Speed: {speed}")



if __name__ == '__main__':
    ranged_damage_stats("Waywatchers")
    print("\n\n")
    ranged_damage_stats("Sisters of Avelorn")
    print("\n\n")
    ranged_damage_stats("Casket of Souls")