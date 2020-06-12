import numpy as np
import pickle
import pandas as pd
from UtilityFunctions import no_nonstandard, average_damage_with_armor_raw

unitsDF = pickle.load( open( "unitsDF.p", "rb" ) )


def ranged_damage_stats(name="",key="",base_dmg_mod=1,ap_dmg_mod=1,reload_buff=0):
    if name == "":
        unit = unitsDF[unitsDF["key"] == key]
    else:
        unit = unitsDF[unitsDF["name"] == name]
        
        if len(unit) > 1:
            raise Exception(f"Amiguous name. Please use one of these key balues\n{unit['key']}")
    
    show_name = unit["name"].values[0]
    
    ap_d = unit["ranged_ap_damage"].values[0]*ap_dmg_mod
    base_d = unit["ranged_base_damage"].values[0]*base_dmg_mod

    num_models = unit["unit_size"].values[0]
    num_proj = unit["projectile_number"].values[0]
    shot_vol = unit["shots_per_volley"].values[0]
    ammo = unit["ammo"].values[0]
    proj_range = unit["range"].values[0]
    caste = unit["caste"].values[0]
    
    base_reload = unit["base_reload_time"].values[0]
    reload_skill = unit["reload_skill"].values[0]+reload_buff
    reload_time = base_reload*(100-reload_skill)/100 # this is probably wrong but it is very close

    calibration_area = unit["calibration_area"].values[0]
    calibration_distance = unit["calibration_distance"].values[0]

    damage_v_60a = average_damage_with_armor_raw(base_d,ap_d,60)

    damage_per_volley_60a = damage_v_60a*num_models*num_proj*shot_vol
    damage_per_ten_60a = damage_per_volley_60a*(10/reload_time)
    damage_per_battle_60a = damage_per_volley_60a*ammo
    
    
    print(f"Some Ranged Damage Stats for {show_name}")
    print(f"{caste}")
    print(f"Range: {int(proj_range)}m")
    print(f"Target Area: {calibration_area}m")
    print(f"Calibration Dist: {calibration_distance}m")
    
    print("\nShooting at 60 Armor")
    print(f"Damage Per Projectile: {int(damage_v_60a)}")
    print(f"Damage Per Volley: {int(damage_per_volley_60a)}")
    print(f"Damage Per 10s: {int(damage_per_ten_60a)}")
    print(f"Damage Per Battle: {int(damage_per_battle_60a)}")
    
    



if __name__ == '__main__':
    ranged_damage_stats("Waywatchers")
    print("\n\n")
    ranged_damage_stats("Sisters of Avelorn")
    print("\n\n")
    ranged_damage_stats("Casket of Souls")
    print("\n\n")
    ranged_damage_stats("Thunderers")
    print("\n\n")
    ranged_damage_stats("Ratling Guns")
    print("\n\n")
    ranged_damage_stats(key="wh2_dlc13_emp_inf_archers_0")