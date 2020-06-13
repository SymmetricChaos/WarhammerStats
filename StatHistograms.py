import numpy as np
import matplotlib.pyplot as plt
import pickle
from UtilityFunctions import no_single_entity, all_from_faction, no_summoned, \
                             no_special_category, no_nonstandard, pretty_name, \
                             code_to_name
from RemoveDuplicates import deduplicate_lore

units = pickle.load( open( "unitsDF.p", "rb" ) )
# Get rid of all nonstandard units like summons, RoR, and campaign units
units = no_nonstandard(units)
# Remove all duplicate casters
units = deduplicate_lore(units)

def histoplot(L,bins=[],percentiles=[],size=[13,6],title=""):
    
    # Coerce bins to a lisy
    bins = list(bins)
    
    fig = plt.figure()
    fig.set_size_inches(size[0], size[1])
    
    if not bins:
        plt.hist(L)
    else:
        plt.hist(L,bins=bins)
        plt.xticks(bins)
        
    plt.title(title,size=20)
    if percentiles:
        percentile_vals = np.nanpercentile(L,np.asarray(percentiles))
        for x in percentile_vals:
            plt.axvline(x,color='black',linewidth=3)
        percentile_legend = []
        for i,j in zip(percentiles,percentile_vals):
             percentile_legend.append(f"{i}th Percentile: {j:.1f}")
        plt.legend(percentile_legend)
    plt.show()


def stats_plot(units,column,faction_code,bins=[]):
    faction_name = code_to_name[faction_code]
    faction_DF =  all_from_faction(units,faction_code)
    histoplot(faction_DF[column],bins,[50],
              title=f"{pretty_name(column)} Distribution\n{faction_name}")



for faction in ["hef","wef","def"]:
    stats_plot(units,"melee_attack",faction,np.arange(0,105,5))