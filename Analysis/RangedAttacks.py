import pickle
from UtilityFunctions import average_damage_with_armor_raw, select_unit


def ranged_damage_stats(unit,target_armor=60,shield=0):
    
    ap_d = unit["ranged_ap_damage"]
    base_d = unit["ranged_base_damage"]
    
    num_models = unit["unit_size"]
    num_proj = unit["projectile_number"]
    shot_vol = unit["shots_per_volley"]
    ammo = unit["ammo"]
    
    base_reload = unit["base_reload_time"]
    reload_skill = unit["reload_skill"]
    reload_time = base_reload*(100-reload_skill)/100 # this is probably wrong but it is very close
    
    calibration_area = unit["calibration_area"]
    calibration_distance = unit["calibration_distance"]
    
    damage_v_a = average_damage_with_armor_raw(base_d,ap_d,target_armor)
    damage_per_volley_a = damage_v_a*num_models*num_proj*shot_vol
    damage_per_ten_a = damage_per_volley_a*(10/reload_time)
    damage_per_battle_a = damage_per_volley_a*ammo
    
    print("## User Facing Stats ##")
    print(unit.unit_card)
    
    print("\n## Hidden Stats ##")
    print(f"Target Area: {calibration_area}m")
    print(f"Calibration Dist: {calibration_distance}m")
    
    print("\n## Derived Stats ##")
    print(f"Shooting at {target_armor} Armor")
    print(f"Damage Per Projectile: {int(damage_v_a)}")
    print(f"Damage Per Volley: {int(damage_per_volley_a)}")
    print(f"Damage Per 10s: {int(damage_per_ten_a)}")
    print(f"Damage Per Battle: {int(damage_per_battle_a)}")
    



if __name__ == '__main__':
    from pathlib import Path
    from TWWObjects import TWWUnit
    
    top_of_path = str(Path(__file__).parent.parent)
    
    unitsDF = pickle.load( open( top_of_path+"\\DataFiles\\unitsDF.p", "rb" ) )

    
    waywatchers = TWWUnit(select_unit(unitsDF,"wh_dlc05_wef_inf_waywatchers_0"))
    waywatchers.toggle_effect("Hawkish Precision")
    ranged_damage_stats(waywatchers)
    print("\n\n")
    ratling = TWWUnit(select_unit(unitsDF,"Ratling Guns"))
    ranged_damage_stats(ratling)