import numpy as np
import matplotlib.pyplot as plt
from UtilityFunctions import average_damage_with_armor_ratio
import pickle

# Defaults armor is max allowed
# Default ap_fractions are the lowest, the two typical, and highest ap_fractions in the
# game
unitsDF = pickle.load( open( "unitsDF.p", "rb" ) )

def armor_graph():
    
    max_armor = 200
    
    max_nat_armor = max(unitsDF["armour"])
    med_armor = np.nanmedian(unitsDF["armour"])
    
    min_ap = min(unitsDF["melee_ap_ratio"])
    max_ap = max(unitsDF["melee_ap_ratio"])
    med_hi_ap = np.nanmedian(unitsDF[unitsDF["melee_ap_ratio"] > .5]["melee_ap_ratio"])
    med_lo_ap = np.nanmedian(unitsDF[unitsDF["melee_ap_ratio"] < .5]["melee_ap_ratio"])
    
    ap_fractions = [min_ap,med_lo_ap,med_hi_ap,max_ap]
    
    armor_lines = [med_armor,max_nat_armor]
    
    legend_descriptions = ["(lowest)","(tyical non-ap)","(typical ap)","(highest)"]
    legend_names = [f"{int(val*100)}% AP {des}" for val,des in zip(ap_fractions,legend_descriptions)]
    armor = np.linspace(0,max_armor,200)
    x_ticks = [i*10 for i in range(0,21)]
    y_ticks = [i for i in range(0,21)]
    
    upper_lims = []
    
    fig = plt.figure()
    fig.set_size_inches(20, 10)
    for ap in ap_fractions:
        hp_mult = [100/average_damage_with_armor_ratio(100,ap,a) for a in armor]
        plt.plot(armor,hp_mult)
        if hp_mult[-1] < 15:
            plt.annotate(f"{round(hp_mult[-1],1)}",(max_armor+1.1,hp_mult[-1]))
        upper_lims.append(hp_mult[-1])
        
    plt.xlabel("Armor")
    plt.ylabel("Effective HP Multiplier")
    
    for xmaj in np.arange(0,200,20):
        plt.axvline(x=xmaj,color='lightgrey',linewidth=1,zorder=-5)
        
    for xmaj in np.arange(10,200,20):
        plt.axvline(x=xmaj,color='lightgrey',linewidth=1.5,zorder=-5)
        
    for ymaj in np.arange(1,20,2):
        plt.axhline(y=ymaj,color='lightgrey',linewidth=1,zorder=-5)
        
    for ymaj in np.arange(2,20,2):
        plt.axhline(y=ymaj,color='lightgrey',linewidth=1.5,zorder=-5)

    plt.legend(legend_names)
    plt.xticks(x_ticks)
    plt.yticks(y_ticks)
    
    plt.ylim([1-max_armor/400,min(max(upper_lims)+1, 15)])
    plt.xlim([-max_armor/20,max_armor+max_armor/20])
    plt.title(f"Impact of Armor as HP Multiplier",size=20)
    
    for vertical in armor_lines:
        plt.axvline(vertical,color='black',linewidth=2)

    plt.annotate("median armor",[med_armor-19,14.1],size=12)
    plt.annotate("highest natural armor",[max_nat_armor-28,14.1],size=12)


if __name__ == '__main__':
    armor_graph()
    
