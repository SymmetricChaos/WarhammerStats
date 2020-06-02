import numpy as np
import pandas as pd
import pickle

# Load the dataframe with the desired information
unitsDF = pickle.load( open( "unitsDF.p", "rb" ) )

## Select the name for every unit with the faction hef.
L = unitsDF.loc[unitsDF['faction'].str.contains('hef')]['name']
for i in L.iloc[:]:
    print(i)
    
print("\n")

## Select a particular row
print(unitsDF.loc[65])

print(unitsDF.loc[unitsDF['key_name'].str.contains('_casket')])