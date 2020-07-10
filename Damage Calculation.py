import math
from UtilityFunctions import melee_hit_prob, average_damage_with_armor_raw, \
                             select_unit
from TWWObjects import TWWUnit
import pickle
effects_dict = pickle.load( open( "effectsDict.p", "rb" ) )

def simulate_attack(attacker,defender,units_attacking=None):
        
    # Very rough estimate of 1/5 units attacking is not specified by user
    if units_attacking == None:
        units_attacking = math.ceil(attacker["unit_size"]*.2)
    
    print("\n## Attacker Stats ##")
    if defender['is_large'] and attacker['melee_bonus_v_large'] > 0 and "BvI" not in attacker.effects:
        print(f"## Including Bonus vs Large of {attacker['melee_bonus_v_large']} ##")
        attacker.toggle_BvL()
    if not defender['is_large'] and attacker['melee_bonus_v_infantry'] > 0 and "BvL" not in attacker.effects:
        print(f"## Including Bonus vs Infantry of {attacker['melee_bonus_v_infantry']} ##")
        attacker.toggle_BvI()
    attacker.unit_card()
    
    print("\n## Defender Stats ##")
    defender.unit_card()
    
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


# Just given a dataframe to draw from and names make a best effort simulation
def simulate_attack_quick(unitsDF,attacker_name,defender_name,
                          units_attacking=None,
                          charge=False,
                          attacker_fatigue="fresh",
                          defender_fatigue="fresh"):
    
    attacker = TWWUnit(select_unit(unitsDF,attacker_name))
    defender = TWWUnit(select_unit(unitsDF,defender_name))
    
    for effect in attacker['abilities']:
        if effect.title() in effects_dict:
            attacker.toggle_effect(effects_dict[effect.title()])
    
    for effect in defender['abilities']:
        if effect.title() in effects_dict:
            defender.toggle_effect(effects_dict[effect.title()])
    
    attacker.set_fatigue(attacker_fatigue)
    defender.set_fatigue(defender_fatigue)
    
    if charge:
        attacker.toggle_charge()
    
    simulate_attack(attacker,defender)





if __name__ == '__main__':
    
    unitsDF = pickle.load( open( "unitsDF.p", "rb" ) )
    
    simulate_attack_quick(unitsDF,"The Fireborn","Firebark",
                          attacker_fatigue = "exhausted")
    print("\n\n\n")
    simulate_attack_quick(unitsDF,"Swordmasters of Hoeth","Skavenslaves",
                          defender_fatigue = "exhausted",
                          charge=True)