import numpy as np
import matplotlib.pyplot as plt
import pickle

units = pickle.load( open( "unitsDF.p", "rb" ) )

def hit_prob(A,D):
    r = 35+A-D
    h = min(max(r,8),90)
    return h/100

def armor_resist(armor):
    ar = np.linspace(armor/2,armor)
    ar = [min(x,100) for x in ar]
    return np.mean(ar)/100

def average_damage(armor,normal_damage,ap_damage,MA,MD):
    hit = hit_prob(MA,MD)
    norma_res = armor_resist(armor)
    return ((normal_damage*(1-norma_res))+ap_damage)*hit
    

test_MD = 32

unit1 = units.iloc[1034]
unit2 = units.iloc[1035]


U1 = []
U2 = []
for i in range(0,101):
    U1.append(average_damage(i,unit1['melee_base_damage'],
                             unit1['melee_ap_damage'],
                             unit1['melee_attack'],MD=test_MD))
    U2.append(average_damage(i,unit2['melee_base_damage'],
                             unit2['melee_ap_damage'],
                             unit2['melee_attack'],MD=test_MD))

plt.figure()
plt.gcf().set_size_inches(10, 8)
plt.plot(U1)
plt.plot(U2)
plt.legend([unit1['name'],unit2['name']])
plt.ylabel("Average Damage")
plt.xlabel("Armor")
plt.xticks(np.arange(0,110,10))
plt.title(f"Average Damage vs Unit with MD={test_MD}",size=20)
plt.grid()