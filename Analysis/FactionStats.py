import numpy as np
import matplotlib.pyplot as plt
import pickle
import pandas as pd
from AnalysisFunctions import histoplot

unitsDF = pickle.load( open( "unitsDF.p", "rb" ) )


helfs = unitsDF.loc[(unitsDF['faction_group'] == 'hef') & (unitsDF['caste'] != "Hero")]
delfs = unitsDF.loc[(unitsDF['faction_group'] == 'def') & (unitsDF['caste'] != "Hero")]
welfs = unitsDF.loc[(unitsDF['faction_group'] == 'wef') & (unitsDF['caste'] != "Hero")]


histoplot(helfs['melee_defence'],np.arange(0,110,5),np.arange(0,110,10),[13,6],
          "High Elf melee_D\nNo Lords or Heroes")

histoplot(delfs['melee_defence'],np.arange(0,110,5),np.arange(0,110,10),[13,6],
          "Dwarf Dmelee_D\nNo Lords or Heroes")


histoplot(welfs['melee_defence'],np.arange(0,110,5),np.arange(0,110,10),[13,6],
          "Wood Elf melee_D\nNo Lords or Heroes")

L = []
for fac in unitsDF['faction_group'].unique():
    if fac == 'hef' or fac == 'def' or fac == 'wef':
        L.append(unitsDF.loc[unitsDF['faction_group'] == str(fac)]['melee_defence'])



histoplot(L,np.arange(0,105,5),np.arange(0,105,5),ranks=[20,50,80])