import numpy as np
import matplotlib.pyplot as plt
from UtilityFunctions import average_damage_with_armor_ratio



def armor_graph(max_armor=200,ap_fractions=[0,.2,.4,.6,.8]):
    
    legend_names = [f"{int(i*100)}% AP" for i in ap_fractions]
    armor = np.linspace(0,max_armor,200)
    x_ticks = [i*10 for i in range(0,21)]
    
    upper_lims = []
    
    fig = plt.figure()
    fig.set_size_inches(16, 8)
    for ap in ap_fractions:
        hp_mult = [100/average_damage_with_armor_ratio(100,ap,a) for a in armor]
        plt.plot(armor,hp_mult)
        plt.annotate(f"{round(hp_mult[-1],1)}",(max_armor+2,hp_mult[-1]))
        upper_lims.append(hp_mult[-1])
        
    plt.xlabel("Armor")
    plt.ylabel("Effective HP Multiplier")
    
    plt.grid()
    plt.legend(legend_names)
    plt.xticks(x_ticks)
    
    plt.ylim([.5,min(max(upper_lims)+1,11)])
    plt.xlim([-5,max_armor+5])
    plt.title(f"HP Multiplier from Armor (0 to {max_armor})",size=20)
    plt.show()



if __name__ == '__main__':
    armor_graph(120)