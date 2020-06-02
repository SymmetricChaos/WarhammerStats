import pickle
import pandas as pd

unitsDF = pickle.load( open( "unitsDF.p", "rb" ) )
pd.set_option('display.max_rows', 500)
print(unitsDF.iloc[0])