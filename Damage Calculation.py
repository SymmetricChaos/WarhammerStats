import numpy as np
import matplotlib.pyplot as plt
import pickle
import math
from UtilityFunctions import melee_hit_prob, average_damage_with_armor_raw, \
                             random_unit, average_armor_reduction
from Fatigue import fatigue_dict

units = pickle.load( open( "unitsDF.p", "rb" ) )

# Need to incorporate passive traits like:
    # regeneration, aura of agony, aura of endurance, aura of pestilence, aura of the lady,
    # bathed in blood, blizzard aura, blinding radiance, crush the weak, enchanting beauty,
    # magical void, martial mastery, martial prowess, fenzy, blessing of the lady, portent of warding
    # power of the dragonback, primal fury, strength in numbers
    # 

def expected_damage_per_melee_attack(attacker,defender,
                                     suppress_abilities=False,
                                     fraction_units_attacking=0.5,
                                     attacker_fatigue="fresh",
                                     defender_fatigue="fresh"):
    
    spacer = max(len(attacker['name']),len(defender['name']))
    
    print(f"Attacker: {attacker['name']:<{spacer}}   {attacker['key']}")
    print(f"Defender: {defender['name']:<{spacer}}   {defender['key']}")
    
    print(f"Attacker is {attacker_fatigue}")
    print(f"Attacker is {defender_fatigue}")
    
    
    att_MA = attacker["melee_attack"]*fatigue_dict[attacker_fatigue]["melee_attack"]
    att_base = attacker["melee_base_damage"]
    att_ap = attacker["melee_ap_damage"]*fatigue_dict[attacker_fatigue]["melee_ap_damage"]
    att_total = attacker["melee_total_damage"]
    att_ratio = attacker["melee_ap_ratio"]
    att_magic = attacker["melee_is_magical"]
    att_flame = attacker["melee_is_flaming"]
    att_flame = attacker["melee_is_flaming"]
    att_flame = attacker["melee_is_flaming"]
    att_BvI = int(max(0,attacker["melee_bonus_v_infantry"]))
    att_BvL = int(max(0,attacker["melee_bonus_v_large"]))
    att_models = attacker["unit_size"]
    att_models_used = math.ceil(att_models*fraction_units_attacking)
    
    print("\nAttacker Stats")
    print(f"MA       = {att_MA}")
    print(f"base-dmg = {att_base}")
    print(f"ap-dmg   = {att_ap}")
    print(f"tot-dmg  = {att_total}")
    print(f"magic    = {att_magic}")
    print(f"flaming  = {att_flame}")
    print(f"BvI      = {att_BvI}")
    print(f"BvL      = {att_BvL}")
    
    
    
    def_MD = defender["melee_defence"]*fatigue_dict[defender_fatigue]["melee_defence"]
    def_armor = defender["armour"]*fatigue_dict[defender_fatigue]["armour"]
    def_physical_res = defender["damage_mod_physical"]
    def_magical_res = defender["damage_mod_magic"]
    def_flame_res = defender["damage_mod_flame"]
    def_ward_res = defender["damage_mod_all"]
    def_large = defender["is_large"]
    
    print("\nDefender Stats")
    print(f"MD       = {def_MD}")
    print(f"armor    = {def_armor}")
    print(f"phys_res = {def_physical_res}%")
    print(f"mag_res  = {def_magical_res}%")
    print(f"fire_res = {def_flame_res}%")
    print(f"ward_res = {def_ward_res}%")
    print(f"large    = {def_large}")
    
    # Effects of BvI and BvL
    if def_large and att_BvL > 0:
        att_MA += att_BvL
        att_base += math.floor(att_BvL*(1-att_ratio))
        att_ap += math.floor(att_BvL*att_ratio)
        
        print("\nBonus vs Infantry")
        print(f"Modified MA       = {att_MA}")
        print(f"Modified base-dmg = {att_base}")
        print(f"Modified ap-dmg   = {att_ap}")
    
    if not def_large and att_BvI > 0:
        att_MA += att_BvI
        att_base += math.floor(att_BvI*(1-att_ratio))
        att_ap += math.floor(att_BvI*att_ratio)
        
        print("\nBonus vs Large")
        print(f"Modified MA       = {att_MA}")
        print(f"Modified base-dmg = {att_base}")
        print(f"Modified ap-dmg   = {att_ap}")
    
    # Probability of an attack to hit
    expected_hit = melee_hit_prob(att_MA,def_MD)
    
    print(f"\nHit Probability = {expected_hit}")
    
    # Armor
    dmg_mul_res = 1-def_ward_res/100
    
    # Magical and physical resistance
    if att_magic:
        dmg_mul_res *= 1-def_magical_res/100
    else:
        dmg_mul_res *= 1-def_physical_res/100
    
    # Fire resist and weakness
    if att_flame:
        dmg_mul_res *= 1-def_flame_res/100
    else:
        pass
    
    # Maximum effect of resistance
    dmg_mul_res = max(dmg_mul_res,.1)
    
    print(f"\nDamage Multiplier From Resistances = {round(dmg_mul_res,2)}")
    
    # Not used, just reported
    dmg_mul_armor = ((1-average_armor_reduction(def_armor))*att_base+att_ap)/(att_base+att_ap)
    
    print(f"Damage Multiplier From Armor = {round(dmg_mul_armor,2)}")
    print(f"Damage Multiplier From All = {round(dmg_mul_armor*dmg_mul_res,2)}")
    
    damage_with_armor = average_damage_with_armor_raw(att_base,att_ap,def_armor)
    avg_dmg = damage_with_armor*dmg_mul_res
    
    print(f"\nExpected Damage Per Attack = {round(max(1,expected_hit*avg_dmg),2)}")






if __name__ == '__main__':
    # Gotta figure out why some results are negative
    unit1 = random_unit(units)
    unit2 = random_unit(units)
    expected_damage_per_melee_attack(unit1,unit2,defender_fatigue="exhausted")