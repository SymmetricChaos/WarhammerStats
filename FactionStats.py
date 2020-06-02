import numpy as np
import matplotlib.pyplot as plt
import pickle
import pandas as pd
from AnalysisFunctions import histoplot

    
unitsDF = pickle.load( open( "unitsDF.p", "rb" ) )

print(unitsDF['class'].unique())
print(unitsDF['faction'].unique())
print(unitsDF['caste'].unique())
print(unitsDF['category'].unique())

helfs = unitsDF.loc[(unitsDF['faction'] == 'hef') & (unitsDF['class'] != "com")]
delfs = unitsDF.loc[(unitsDF['faction'] == 'def') & (unitsDF['class'] != "com")]
welfs = unitsDF.loc[(unitsDF['faction'] == 'wef') & (unitsDF['class'] != "com")]


histoplot(helfs['melee_D'],np.arange(0,110,5),np.arange(0,110,10),[13,6],
          "High Elf melee_D\nNo Lords or Heroes")

histoplot(delfs['melee_D'],np.arange(0,110,5),np.arange(0,110,10),[13,6],
          "Dwarf Dmelee_D\nNo Lords or Heroes")


histoplot(welfs['melee_D'],np.arange(0,110,5),np.arange(0,110,10),[13,6],
          "Wood Elf melee_D\nNo Lords or Heroes")

L = []
for fac in unitsDF['faction'].unique():
    if fac == 'hef' or fac == 'def' or fac == 'wef':
        L.append(unitsDF.loc[unitsDF['faction'] == str(fac)]['melee_D'])



histoplot(L,np.arange(0,105,5),np.arange(0,105,5),ranks=[20,50,80])