import pickle
from UtilityFunctions import select_unit
from TWWObjects import TWWUnit

unitsDF = pickle.load( open( "unitsDF.p", "rb" ) )

effects_dict = pickle.load( open( "effectsDict.p", "rb" ) )

# for i in unitsDF['key']:
#     unit = TWWUnit(select_unit(unitsDF,i))
#     unit.unit_card

for e in effects_dict:
    if e == "Weeping Blade":
        print(effects_dict[e].display())