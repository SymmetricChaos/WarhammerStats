import matplotlib.pyplot as plt
import pickle
import math
import pandas as pd
from UtilityFunctions import melee_hit_prob, average_damage_with_armor_raw, \
                             random_unit, average_armor_reduction, select_unit
from Fatigue import fatigue_dict


# Need to incorporate passive traits like:
    # regeneration, aura of agony, aura of endurance, aura of pestilence, aura of the lady,
    # bathed in blood, blizzard aura, blinding radiance, crush the weak, enchanting beauty,
    # magical void, martial mastery, martial prowess, fenzy, blessing of the lady, portent of warding
    # power of the dragonback, primal fury, strength in numbers
    # 

# Conditions and abilities that affect self

def apply_fatigue_effects(unit,fatigue_level="fresh"):
    unit["melee_attack"] = math.ceil(unit["melee_attack"]*fatigue_dict[fatigue_level]["melee_attack"])
    unit["melee_ap_damage"] = math.ceil(unit["melee_ap_damage"]*fatigue_dict[fatigue_level]["melee_ap_damage"])
    unit["melee_defence"] = math.ceil(unit["melee_defence"]*fatigue_dict[fatigue_level]["melee_defence"])
    unit["armour"] = math.ceil(unit["armour"]*fatigue_dict[fatigue_level]["armour"])
    unit["charge_bonus"] = math.ceil(unit["charge_bonus"]*fatigue_dict[fatigue_level]["charge_bonus"])
    unit["melee_total_damage"] = unit["melee_base_damage"]+unit["melee_ap_damage"]

def apply_BvI(unit):
    BvI = unit["melee_bonus_v_infantry"]
    ap_ratio = unit["melee_ap_ratio"]
    unit["melee_attack"] += BvI
    unit["melee_base_damage"] += math.floor(BvI*(1-ap_ratio))
    unit["melee_ap_damage"] += math.floor(BvI*(ap_ratio))
    unit["melee_total_damage"] = unit["melee_base_damage"]+unit["melee_ap_damage"]

def apply_BvL(unit):
    BvL = unit["melee_bonus_v_large"]
    ap_ratio = unit["melee_ap_ratio"]
    unit["melee_attack"] += BvL
    unit["melee_base_damage"] += math.floor(BvL*(1-ap_ratio))
    unit["melee_ap_damage"] += math.floor(BvL*(ap_ratio))
    unit["melee_total_damage"] = unit["melee_base_damage"]+unit["melee_ap_damage"]
    
def apply_stand_your_ground(unit):
    unit["melee_defence"] += 5
    
def apply_evasion(unit):
    unit["melee_defence"] += 5
    
def apply_bathed_in_blood(unit):
    unit["melee_attack"] += 5
    
def apply_freny(unit):
    unit["melee_attack"] += 8
    unit["melee_base_damage"] = math.ceil(unit["melee_base_damage"]*1.15)
    unit["melee_total_damage"] = unit["melee_base_damage"]+unit["melee_ap_damage"]
    
def apply_aura_of_protection(unit):
    unit['damage_mod_all'] += 12
    
def apply_primal_fury(unit):
    unit['melee_attack'] += 5
    
def apply_the_dark_mail(unit):
    unit['armour'] += 30
    unit['damage_mod_magic'] += 25
    
def apply_regeneration(unit):
    unit['damage_mod_flame'] -= 25
    
def apply_slaughterers_call(unit):
    unit['melee_attack'] += 9
    
def apply_braid_of_bordelaux(unit):
    unit['melee_bonus_v_large'] += 8
    
def apply_fleur_de_lys_banner(unit):
    unit['melee_attack'] += 9
    unit['melee_defence'] += 9
    
def apply_aura_of_the_lady(unit):
    unit['damage_mod_magic'] += 12
    
def apply_blessing_of_the_lady(unit):
    unit['damage_mod_physical'] += 20
    

    
    
    
    
# Abilities that affect enemies
def apply_crush_the_weak(unit):
    unit["melee_attack"] -= 5
    unit["melee_defence"] -= 5
    
def apply_the_white_cloak_of_ulric(unit):
    unit["melee_attack"] -= 9
    
def apply_blinding_radiance(unit):
    unit["melee_attack"] -= 9
    
def apply_mist_of_the_lady(unit):
    unit['melee_attack'] -= 5




# Deal with specifying names
# Copy technique from that other file

def expected_damage_per_melee_attack(unitsDF,attacker_name,defender_name,
                                     fraction_units_attacking=0.2,
                                     attacker_fatigue="fresh",
                                     defender_fatigue="fresh"):
    
    attacker = select_unit(unitsDF,attacker_name)
    defender = select_unit(unitsDF,defender_name)
    
    spacer = max(len(attacker['name']),len(defender['name']))
    
    print(f"Attacker: {attacker['name']:<{spacer}}   {attacker['key']}")
    print(f"Defender: {defender['name']:<{spacer}}   {defender['key']}")
    
    print(f"\nAttacker is {attacker_fatigue}")
    print(f"Defender is {defender_fatigue}")
    
    
    # print(attacker['abilities'])
    # print(defender['abilities'])
    
    
    apply_fatigue_effects(attacker,attacker_fatigue)
    apply_fatigue_effects(defender,defender_fatigue)
    
    att_models_used = math.ceil(attacker["unit_size"]*fraction_units_attacking)
    
    print("\n## Attacker Stats ##")
    print(f"MA       = {attacker['melee_attack']}")
    print(f"base-dmg = {attacker['melee_base_damage']}")
    print(f"ap-dmg   = {attacker['melee_ap_damage']}")
    print(f"tot-dmg  = {attacker['melee_total_damage']}")
    print(f"magic    = {attacker['melee_is_magical']}")
    print(f"flaming  = {attacker['melee_is_flaming']}")
    print(f"BvI      = {attacker['melee_bonus_v_infantry']}")
    print(f"BvL      = {attacker['melee_bonus_v_large']}")
    
    
    print("\n## Defender Stats ##")
    print(f"MD       = {defender['melee_defence']}")
    print(f"armor    = {defender['armour']}")
    print(f"phys_res = {defender['damage_mod_physical']}%")
    print(f"mag_res  = {defender['damage_mod_magic']}%")
    print(f"fire_res = {defender['damage_mod_flame']}%")
    print(f"ward_res = {defender['damage_mod_all']}%")
    print(f"large    = {defender['is_large']}")
    
    # # Effects of BvI and BvL
    if defender['is_large'] and attacker['melee_bonus_v_large'] > 0:
        apply_BvL(attacker)
        print("\nAttacker Bonus vs Infantry")
        print(f"MA       = {attacker['melee_attack']}")
        print(f"base-dmg = {attacker['melee_base_damage']}")
        print(f"ap-dmg   = {attacker['melee_ap_damage']}")
        print(f"tot-dmg  = {attacker['melee_total_damage']}")
    
    if not defender['is_large'] and attacker['melee_bonus_v_infantry'] > 0:
        apply_BvI(attacker)
        print("\nAttacker Bonus vs Infantry")
        print(f"MA       = {attacker['melee_attack']}")
        print(f"base-dmg = {attacker['melee_base_damage']}")
        print(f"ap-dmg   = {attacker['melee_ap_damage']}")
        print(f"tot-dmg  = {attacker['melee_total_damage']}")
    
    # Probability of an attack to hit
    expected_hit = melee_hit_prob(attacker['melee_attack'],defender['melee_defence'])
    
    print(f"\nHit Probability = {expected_hit}")
    
    # Ward save
    dmg_mul_res = 1-defender['damage_mod_all']/100
    
    # Magical and physical resistance
    if attacker['melee_is_magical']:
        dmg_mul_res *= 1-defender['damage_mod_magic']/100
    else:
        dmg_mul_res *= 1-defender['damage_mod_physical']/100
    
    # Fire resist and weakness
    if attacker['melee_is_flaming']:
        dmg_mul_res *= 1-defender['damage_mod_flame']/100

    
    # Maximum effect of resistance
    dmg_mul_res = max(dmg_mul_res,.1)
    
    print(f"\nDamage Multiplier From Resistances = {round(dmg_mul_res,2)}")
    
    # Not used, just reported
    armor_mul_base = 1-average_armor_reduction(defender['armour'])
    dmg_mul_armor = (armor_mul_base * attacker['melee_base_damage']
                     +attacker['melee_ap_damage'])/(attacker['melee_total_damage'])
    
    print(f"Damage Multiplier From Armor = {round(dmg_mul_armor,2)}")
    print(f"Damage Multiplier From All = {round(dmg_mul_armor*dmg_mul_res,2)}")
    
    damage_with_armor = average_damage_with_armor_raw(attacker['melee_base_damage'],
                                                      attacker['melee_ap_damage'],
                                                      defender['armour'])
    avg_dmg = damage_with_armor*dmg_mul_res
    
    print(f"\nExpected Damage Per Attack = {round(max(1,expected_hit*avg_dmg),2)}"
          f"\n\nAssuming {att_models_used} "
          f"{'Unit Attacks' if att_models_used == 1 else 'Units Attack'}"
          "\nTotal Expected Damage = "
          f"{round(max(1,expected_hit*avg_dmg*att_models_used),2)}")





if __name__ == '__main__':
    unitsDF = pickle.load( open( "unitsDF.p", "rb" ) )

    # unit1 = random_unit(unitsDF)
    # print(type(unit1))
    # unit2 = random_unit(units)
    expected_damage_per_melee_attack(unitsDF,"The Fireborn","Durthu")