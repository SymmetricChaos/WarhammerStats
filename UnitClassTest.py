import pickle
from UtilityFunctions import select_unit
from TWWObjects import TWWUnit
effects_dict = pickle.load( open( "effectsDict.p", "rb" ) )

unitsDF = pickle.load( open( "unitsDF.p", "rb" ) )

my_unit = TWWUnit(select_unit(unitsDF,"Phoenix Guard"))

print(my_unit)

print("\nTest Bonus Vs Large")
print("Currently it is off")
my_unit.unit_card()

my_unit.toggle_BvL()
print("Toggled to on")
my_unit.unit_card()

my_unit.toggle_BvL()
print("Toggled back off")
my_unit.unit_card()





print("\n\n\nTest Effects")

my_unit.toggle_effect(effects_dict["Martial Mastery"])
my_unit.unit_card()

my_unit.toggle_effect(effects_dict["Stand Your Ground!"])
my_unit.unit_card()

my_unit.toggle_effect(effects_dict["Poison"])
my_unit.unit_card()

my_unit.toggle_effect(effects_dict["Martial Mastery"])
my_unit.unit_card()

my_unit.toggle_effect(effects_dict["Poison"])
my_unit.unit_card()

my_unit.toggle_effect(effects_dict["Stand Your Ground!"])
my_unit.unit_card()