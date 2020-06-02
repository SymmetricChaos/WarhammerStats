import numpy as np
import matplotlib.pyplot as plt

ap_fraction = np.array([0,.1,.2,.3,.4,.7])
legend_labels = ["0% AP: No Unit","10% AP: Crypt Ghouls","20% AP: Skinks","30% AP: Knights Errant",
                 "40% AP: Grail Knights", "70% AP: Minotaurs"]
legend_names = ["{:.0f}% AP".format(i*100) for i in ap_fraction]
armor = np.arange(0,201,1)
x_ticks = [i*10 for i in range(0,21)]

def damage_blocked(i):
    ar = np.linspace(i/2,i)
    ar = [min(x,100) for x in ar]
    return np.mean(ar)

non_ap_blocked = np.array([damage_blocked(i) for i in armor])

fig = plt.figure()
fig.set_size_inches(16, 8)
for ap in ap_fraction:
    y = (1-ap)*non_ap_blocked
    hp_mult = 1/(1-y/100)
    plt.plot(armor,hp_mult)
    if ap != 0:
        plt.annotate("{:.1f}".format(hp_mult[-1]),(202,hp_mult[-1]))
    
plt.xlabel("Armor")
plt.ylabel("Effective HP Multiplier")
plt.grid()
plt.legend(legend_names)
plt.xticks(x_ticks)
plt.ylim([.5,11])
plt.title("HP Multiplier from Armor",size=20)
plt.show()



fig = plt.figure()
fig.set_size_inches(16, 8)
for ap in ap_fraction:
    y = (1-ap)*non_ap_blocked[:121]
    hp_mult = 1/(1-y/100)
    plt.plot(armor[:121],hp_mult)
    if ap != 0:
        plt.annotate("{:.1f}".format(hp_mult[-1]),(121,hp_mult[-1]))

    
plt.xlabel("Armor")
plt.ylabel("Effective HP Multiplier")
plt.grid()
plt.legend(legend_labels)
plt.xticks(x_ticks[:13])
plt.ylim([.5,5])
plt.title("HP Multiplier from Armor (0 to 120)",size=20)
plt.show()
