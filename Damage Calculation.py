import numpy as np
import matplotlib.pyplot as plt
import pickle
from UtilityFunctions import melee_hit_prob, average_damage_with_armor_raw, \
                             random_unit, average_armor_reduction

units = pickle.load( open( "unitsDF.p", "rb" ) )

def expected_damage_per_melee_attack(attacker,defender):
    
    print(f"Attacker: {attacker['name']}")
    print(f"Defender: {defender['name']}")
    
    
    att_MA = attacker["melee_attack"]
    att_base = attacker["melee_base_damage"]
    att_ap = attacker["melee_ap_damage"]
    att_total = attacker["melee_total_damage"]
    att_magic = attacker["melee_is_magical"]
    att_flame = attacker["melee_is_flaming"]
    
    print("\nAttacker Stats")
    print(f"MA       = {att_MA}")
    print(f"base-dmg = {att_base}")
    print(f"ap-dmg   = {att_ap}")
    print(f"tot-dmg  = {att_total}")
    print(f"magic    = {att_magic}")
    print(f"flaming  = {att_flame}")
    
    
    def_MD = defender["melee_defence"]
    def_armor = defender["armour"]
    def_physical_res = defender["damage_mod_physical"]
    def_magical_res = defender["damage_mod_magic"]
    def_flame_res = defender["damage_mod_flame"]
    def_ward_res = defender["damage_mod_all"]
    
    print("\nDefender Stats")
    print(f"MD       = {def_MD}")
    print(f"armor    = {def_armor}")
    print(f"phys_res = {def_physical_res}%")
    print(f"mag_res  = {def_magical_res}%")
    print(f"fire_res = {def_flame_res}%")
    print(f"ward_res = {def_ward_res}%")
    
    
    
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
    
    if att_flame:
        dmg_mul_res *= 1-def_flame_res/100
    else:
        pass
    
    
    
    dmg_mul_res = max(dmg_mul_res,.1)
    
    print(f"\nDamage Multiplier From Resistances = {dmg_mul_res}")
    
    # Not used, just reported
    dmg_mul_armor = ((1-average_armor_reduction(def_armor))*att_base+att_ap)/(att_base+att_ap)
    
    print(f"Damage Multiplier From Armor = {dmg_mul_armor}")
    print(f"Damage Multiplier From All = {dmg_mul_armor*dmg_mul_res}")
    
    
    damage_with_armor = average_damage_with_armor_raw(att_base,att_ap,def_armor)
    avg_dmg = damage_with_armor*dmg_mul_res
    
    print(f"\nExpected Damage Per Attack = {max(1,expected_hit*avg_dmg)}")






if __name__ == '__main__':
    # Gotta figure out why some results are negative
    unit1 = random_unit(units)
    unit2 = random_unit(units)
    expected_damage_per_melee_attack(unit1,unit2)





# U1 = []
# U2 = []
# for i in range(0,101):
#     U1.append(average_damage(i,unit1['melee_base_damage'],
#                              unit1['melee_ap_damage'],
#                              unit1['melee_attack'],MD=test_MD))
#     U2.append(average_damage(i,unit2['melee_base_damage'],
#                              unit2['melee_ap_damage'],
#                              unit2['melee_attack'],MD=test_MD))

# plt.figure()
# plt.gcf().set_size_inches(10, 8)
# plt.plot(U1)
# plt.plot(U2)
# plt.legend([unit1['name'],unit2['name']])
# plt.ylabel("Average Damage")
# plt.xlabel("Armor")
# plt.xticks(np.arange(0,110,10))
# plt.title(f"Average Damage vs Unit with MD={test_MD}",size=20)
# plt.grid()