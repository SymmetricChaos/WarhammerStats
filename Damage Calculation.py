import numpy as np
import matplotlib.pyplot as plt
import pickle

units = pickle.load( open( "unitsDict.p", "rb" ) )

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
    

def read_index(n):
    for stat,val in units.items():
        print("{:<15}: {}".format(stat,val[n]))

unit1 = units['key_name'].index("wh_main_chs_inf_chosen_1")
unit2 = units['key_name'].index("wh_main_chs_inf_chosen_0")

read_index(unit1)
print("\n")
read_index(unit2)


U1 = []
U2 = []
for i in range(0,201):
    U1.append(average_damage(i,units['damage'][unit1],units['ap_damage'][unit1],units['melee_A'][unit1],MD=32))
    U2.append(average_damage(i,units['damage'][unit2],units['ap_damage'][unit2],units['melee_A'][unit2],MD=32))

plt.figure()
plt.gcf().set_size_inches(12, 6)
plt.plot(U1)
plt.plot(U2)
plt.legend([units['name'][unit1],units['name'][unit2]])
plt.ylabel("Average Damage")
plt.xlabel("Armor")
plt.xticks(np.arange(0,210,10))
plt.title("Average Damage vs Unit with MD=32",size=20)
plt.grid()