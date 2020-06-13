import numpy as np
import pickle
import pandas as pd
from UtilityFunctions import no_nonstandard, average_damage_with_armor_raw

unitsDF = pickle.load( open( "unitsDF.p", "rb" ) )


def ranged_damage_stats(name,base_dmg_mod=1,ap_dmg_mod=1,reload_buff=0):
    
    unit = unitsDF[unitsDF["name"].str.contains(name)]
    if len(unit) == 0:
        unit = unitsDF[unitsDF["key"] == name]
        if len(unit) == 0:
            raise Exception(f"{name} is not a unit name or key")
    if len(unit) > 1:
        raise Exception(f"Ambiguous name. Please use one of these key values\n{unit['key'].values}")
    
    show_name = unit["name"].values[0]
    
    ap_d = unit["ranged_ap_damage"].values[0]*ap_dmg_mod
    base_d = unit["ranged_base_damage"].values[0]*base_dmg_mod

    num_models = unit["unit_size"].values[0]
    num_proj = unit["projectile_number"].values[0]
    shot_vol = unit["shots_per_volley"].values[0]
    ammo = unit["ammo"].values[0]
    proj_range = unit["range"].values[0]
    
    caste = unit["caste"].values[0]
    category = unit["category"].values[0]
    
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
    if caste == category:
        print(f"{caste}\n")
    else:
        print(f"{caste}: {category}\n")
    
    print(f"Range: {int(proj_range)}m")
    print(f"Target Area: {calibration_area}m")
    print(f"Calibration Dist: {calibration_distance}m")
    
    print("\nShooting at 60 Armor")
    print(f"Damage Per Projectile: {int(damage_v_60a)}")
    print(f"Damage Per Volley: {int(damage_per_volley_60a)}")
    print(f"Damage Per 10s: {int(damage_per_ten_60a)}")
    print(f"Damage Per Battle: {int(damage_per_battle_60a)}")
    
    



if __name__ == '__main__':
    ranged_damage_stats("wh_dlc05_wef_inf_waywatchers_0")
    print("\n\n")
    ranged_damage_stats("wh2_dlc10_hef_inf_sisters_of_avelorn_0")
    print("\n\n")
    ranged_damage_stats("wh2_dlc09_tmb_art_casket_of_souls_0")
    print("\n\n")
    ranged_damage_stats("Thunderers")
    print("\n\n")
    ranged_damage_stats("wh2_dlc12_skv_inf_ratling_gun_0")
    print("\n\n")
    ranged_damage_stats("wh2_dlc13_emp_inf_archers_0")
    print("\n\n")
    ranged_damage_stats("wh_main_emp_cav_pistoliers_1")