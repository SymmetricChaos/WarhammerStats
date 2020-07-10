import pickle
from UtilityFunctions import select_unit
from TWWObjects import TWWUnit

unitsDF = pickle.load( open( "unitsDF.p", "rb" ) )

for i in unitsDF['key']:
    unit = TWWUnit(select_unit(unitsDF,i))
    unit.unit_card()
