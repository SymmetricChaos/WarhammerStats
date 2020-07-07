import math
from UtilityFunctions import melee_hit_prob, average_damage_with_armor_raw, \
                             select_unit
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

def apply_charge(unit):
    charge = unit["charge_bonus"]
    ap_ratio = unit["melee_ap_ratio"]
    unit["melee_attack"] += charge
    unit["melee_base_damage"] += math.floor(charge*(1-ap_ratio))
    unit["melee_ap_damage"] += math.floor(charge*(ap_ratio))
    unit["melee_total_damage"] = unit["melee_base_damage"]+unit["melee_ap_damage"]



# Deal with specifying names
# Copy technique from that other file

def expected_damage_per_melee_attack(unitsDF,attacker_name,defender_name,
                                     units_attacking=None,
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
    
    # Very rough estimate of 1/5 units attacking is not specified by user
    if units_attacking == None:
        units_attacking = math.ceil(attacker["unit_size"]*.2)
    
    
    print("\n## Attacker Stats ##")
    if defender['is_large'] and attacker['melee_bonus_v_large'] > 0:
        print(f"## Including Bonus vs Large of {attacker['melee_bonus_v_large']} ##")
        apply_BvL(attacker)
    if not defender['is_large'] and attacker['melee_bonus_v_infantry'] > 0:
        print(f"## Including Bonus vs Infantry of {attacker['melee_bonus_v_infantry']} ##")
        apply_BvI(attacker)
    
    print(f"MA       = {attacker['melee_attack']}")
    print(f"base-dmg = {attacker['melee_base_damage']}")
    print(f"ap-dmg   = {attacker['melee_ap_damage']}")
    print(f"tot-dmg  = {attacker['melee_total_damage']}")
    print(f"magic    = {attacker['melee_is_magical']}")
    print(f"flaming  = {attacker['melee_is_flaming']}")
    
    
    
    print("\n## Defender Stats ##")
    print(f"MD       = {defender['melee_defence']:>4}")
    print(f"armor    = {defender['armour']:>4}")
    print(f"phys_res = {defender['damage_mod_physical']:>3}%")
    print(f"mag_res  = {defender['damage_mod_magic']:>3}%")
    print(f"fire_res = {defender['damage_mod_flame']:>3}%")
    print(f"ward_res = {defender['damage_mod_all']:>3}%")
    print(f"large    = {defender['is_large']:>4}")

    
    # Probability of an attack to hit
    expected_hit = melee_hit_prob(attacker['melee_attack'],defender['melee_defence'])
    
    print(f"\nHit Probability = {expected_hit}")
    
    # Damage that gets through armour
    # Resistances are then applied to this value
    damage_with_armor = average_damage_with_armor_raw(attacker['melee_base_damage'],
                                                      attacker['melee_ap_damage'],
                                                      defender['armour'])
    
    print(f"\nDamage After Armor = {math.ceil(damage_with_armor)}")
    
    # Ward save
    dmg_mul_res = defender['damage_mod_all']
    
    # Magical and physical resistance
    if attacker['melee_is_magical']:
        dmg_mul_res += defender['damage_mod_magic']
    else:
        dmg_mul_res += defender['damage_mod_physical']
    
    # Fire resist and weakness
    if attacker['melee_is_flaming']:
        dmg_mul_res += defender['damage_mod_flame']
    
    # Maximum effect of resistance
    dmg_mul_res = 1-(dmg_mul_res/100)
    dmg_mul_res = max(dmg_mul_res,.1)
    
    
    print(f"\nDamage Multiplier From Resistances = {round(dmg_mul_res,2)}")
    
    avg_dmg = damage_with_armor*dmg_mul_res
    
    print(f"\nExpected Damage Per Attack = {round(max(1,expected_hit*avg_dmg),2)}"
          f"\n\nAssuming {units_attacking} "
          f"{'Unit Attacks' if units_attacking == 1 else 'Units Attack'}"
          "\nTotal Expected Damage = "
          f"{round(max(1,expected_hit*avg_dmg*units_attacking),2)}")





if __name__ == '__main__':
    import pickle
    unitsDF = pickle.load( open( "unitsDF.p", "rb" ) )

    expected_damage_per_melee_attack(unitsDF,"The Fireborn","Firebark",
                                     attacker_fatigue = "exhausted")
    print("\n\n\n")
    expected_damage_per_melee_attack(unitsDF,"Swordmasters of Hoeth","Skavenslaves",
                                     defender_fatigue = "exhausted")