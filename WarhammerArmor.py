import numpy as np
import matplotlib.pyplot as plt
from UtilityFunctions import average_damage_with_armor_ratio


# Defaults armor is max allowed
# Default ap_fractions are the lowest, median, and highest ap_fractions in the
# game
def armor_graph(max_armor=200,ap_fractions=[.07,.33,.88],armor_lines=[60,160]):
    
    legend_names = [f"{int(i*100)}% AP" for i in ap_fractions]
    armor = np.linspace(0,max_armor,200)
    x_ticks = [i*10 for i in range(0,21)]
    y_ticks = [i for i in range(0,21)]
    
    upper_lims = []
    
    fig = plt.figure()
    fig.set_size_inches(16, 8)
    for ap in ap_fractions:
        hp_mult = [100/average_damage_with_armor_ratio(100,ap,a) for a in armor]
        plt.plot(armor,hp_mult)
        if hp_mult[-1] < 15:
            plt.annotate(f"{round(hp_mult[-1],1)}",(max_armor+1.1,hp_mult[-1]))
        upper_lims.append(hp_mult[-1])
        
    plt.xlabel("Armor")
    plt.ylabel("Effective HP Multiplier")
    
    plt.grid()
    plt.legend(legend_names)
    plt.xticks(x_ticks)
    plt.yticks(y_ticks)
    
    plt.ylim([1-max_armor/400,min(max(upper_lims)+1, 15)])
    plt.xlim([-max_armor/20,max_armor+max_armor/20])
    plt.title(f"HP Multiplier from Armor (0 to {max_armor})",size=20)
    
    for vertical in armor_lines:
        plt.axvline(vertical,color='black',linewidth=2)




if __name__ == '__main__':
    armor_graph()
    plt.annotate("median armor",[37,14.1],size=12)
    plt.annotate("highest natural armor",[125,14.1],size=12)