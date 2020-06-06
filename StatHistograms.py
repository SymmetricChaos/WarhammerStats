import numpy as np
import matplotlib.pyplot as plt
import pickle
from UtilityFunctions import no_single_entity, all_from_faction, no_summoned, \
                             no_special_category

units = pickle.load( open( "unitsDF.p", "rb" ) )
# Get rid of summon units
units = no_summoned(units)

brt = all_from_faction(units,'brt')
bst = all_from_faction(units,'bst')
chs = all_from_faction(units,'chs')
cst = all_from_faction(units,'cst')
dlf = all_from_faction(units,'def')
dwf = all_from_faction(units,'dwf')
emp = all_from_faction(units,'emp')
grn = all_from_faction(units,'grn')
hef = all_from_faction(units,'hef')
lzd = all_from_faction(units,'lzd')
nor = all_from_faction(units,'nor')
skv = all_from_faction(units,'skv')
tmb = all_from_faction(units,'tmb')
vmp = all_from_faction(units,'vmp')
wef = all_from_faction(units,'wef')


def histoplot(L,bins,x_ticks,size=[13,6],title=""):
    
    
    fig = plt.figure()
    fig.set_size_inches(size[0], size[1])
    plt.hist(L,bins=bins)
    plt.xticks(x_ticks)
    plt.title(title,size=20)
    percentiles = np.nanpercentile(L,[20,50,80])
    for x in percentiles:
        plt.axvline(x,color='black',linewidth=3)
    percentile_legend = []
    for i,j in zip(['20','50','80'],percentiles):
         percentile_legend.append("{}th Percentile: {:.1f}".format(i,j))
    plt.legend(percentile_legend)
    plt.show()


#histoplot(units['armour'],np.arange(0,210,10),[i*10 for i in range(0,21)],[13,6],
#          "Armor Distribution\nWith 20th, 50th, 80th Percentiles")
#
#
#histoplot(units['melee_attack'],np.arange(0,105,5),[i*5 for i in range(0,21)],[13,6],
#          "Melee Attack Distribution\nWith 20th, 50th, 80th Percentiles")
#
#histoplot(units['melee_defence'],np.arange(0,105,5),[i*5 for i in range(0,21)],[13,6],
#          "Melee Defense Distribution\nWith 20th, 50th, 80th Percentiles")
#
#histoplot(units['melee_total_damage'],np.arange(0,600,20),[i*20 for i in range(0,31)],[13,6],
#          "Total Damage Distribution\nWith 20th, 50th, 80th Percentiles")
#
#histoplot(units['melee_ap_ratio'],np.arange(0,1,.05),np.arange(0,1,.05),[13,6],
#          "AP Ratio Distribution\nWith 20th, 50th, 80th Percentiles")
#
#
#no_single = no_single_entity(units)
#
#histoplot(no_single['melee_ap_ratio'],np.arange(0,1,.05),np.arange(0,1,.05),[13,6],
#          "AP Ratio Distribution (No Single Entities)\nWith 20th, 50th, 80th Percentiles")
#
#histoplot(no_single['armour'],np.arange(0,200,10),np.arange(0,200,10),[13,6],
#          "Armor Distribution (No Single Entities)\nWith 20th, 50th, 80th Percentiles")

factions = [brt,bst,chs,cst,dlf,dwf,emp,grn,hef,lzd,nor,skv,tmb,vmp,wef]
faction_names = ["Brettonia","Beastmen","Warriors of Chaos","Vampire Coast",
                 "Dark Elves","Dwarfs","Empire","Greenskins","High Elves",
                 "Lizardmen","Norsca","Skaven","Tomb Kings","Vampire Counts",
                 "Wood Elves"]
for code,name in zip(factions,faction_names):
    histoplot(code['armour'],np.arange(0,210,10),[i*10 for i in range(0,21)],[13,6],
              f"Armor Distribution\n{name}")