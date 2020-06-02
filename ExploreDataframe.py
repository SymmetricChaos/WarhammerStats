import pickle
import pandas as pd
import numpy as np

unitsDF = pickle.load( open( "unitsDF.p", "rb" ) )
pd.set_option('display.max_rows', 500)

r, = np.random.randint(0,1365,1)

print(unitsDF.iloc[r])

for name in unitsDF['name'].unique():
    if "UNIT" in name:
        print(name)