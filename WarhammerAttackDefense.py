import numpy as np
import matplotlib.pyplot as plt

Melee_Attack = np.arange(30,70,10)
Melee_Defense = np.arange(0,100,5)
legend_names = ["MA = {:.0f}".format(i) for i in Melee_Attack]
x_ticks = [i*10 for i in range(0,10)]
#y_ticks = np.linspace(0,1,11)

def hit_prob(MA,MD):
    x = 35+MA-MD
    if x > 90:
        x = 90
    if x < 8:
        x = 8
    return x/100

#non_ap_blocked = np.array([damage_blocked(i) for i in armor])

fig = plt.figure()
fig.set_size_inches(16, 8)
for MA in Melee_Attack:
    hit = np.array([hit_prob(MA,d) for d in Melee_Defense])
    effective_resist = 1-hit
    hp_mult = 1/(1-effective_resist)
    plt.plot(Melee_Defense,hp_mult)
    
plt.xlabel("Melee Defense")
plt.ylabel("HP Multiplier")
plt.grid()
plt.legend(legend_names)
plt.xticks(x_ticks)
#plt.yticks(y_ticks)
plt.show()

