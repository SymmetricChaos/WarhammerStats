import numpy as np
import matplotlib.pyplot as plt
import pickle
import pandas as pd


def histoplot(L,bins,x_ticks,size=[13,6],title="",percentile_marks=True,stacked=True):
    
    
    fig = plt.figure()
    fig.set_size_inches(size[0], size[1])
    H = plt.hist(L,bins=bins,stacked=stacked)
    plt.xticks(x_ticks)
    plt.title(title,size=20)
    if percentile_marks:
        percentiles = np.percentile(L,[20,50,80])
        for x in percentiles:
            plt.axvline(x,color='black',linewidth=3)
            percentile_legend = []
            for i,j in zip(['20','50','80'],percentiles):
                percentile_legend.append("{}th Percentile: {:.1f}".format(i,j))
        plt.legend(percentile_legend)
        
    return H


    
unitsDF = pickle.load( open( "unitsDF.p", "rb" ) )

L = unitsDF['ap_fraction'].values
Lnap  = [i for i in L if i < .5]
Lap = [i for i in L if i >= .5]

histoplot([Lap,Lnap],np.linspace(0,1,21),np.linspace(0,1,11),
          percentile_marks=False)
plt.axvline(np.median(Lap),color='black',linewidth=3)
plt.axvline(np.median(Lnap),color='black',linewidth=3)
plt.title("AP vs NonAP Split",size=20)

Lnap_units =  unitsDF.loc[(unitsDF['ap_fraction']  <= .5) & (unitsDF['caste'] == 'melee_infantry')]
Lap_units =  unitsDF.loc[(unitsDF['ap_fraction']  > .5) & (unitsDF['caste'] == 'melee_infantry')]

print(np.median(Lnap_units['total_damage'].values))
print(np.median(Lap_units['total_damage'].values))