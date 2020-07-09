import pickle
from UtilityFunctions import select_unit
from TWWObjects import TWWUnit, TWWEffect

unitsDF = pickle.load( open( "unitsDF.p", "rb" ) )
stat_effects = pickle.load( open( "stat_effects.p", "rb" ) )

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





print("\n\n\nTest Martial Mastery")
my_unit.unit_card()

my_unit.toggle_effect(stat_effects["Martial Mastery"])
my_unit.unit_card()

my_unit.toggle_effect(stat_effects["Stand Your Ground"])
my_unit.unit_card()

my_unit.toggle_effect(stat_effects["Poison"])
my_unit.unit_card()

my_unit.toggle_effect(stat_effects["Martial Mastery"])
my_unit.unit_card()

my_unit.toggle_effect(stat_effects["Poison"])
my_unit.unit_card()

my_unit.toggle_effect(stat_effects["Stand Your Ground"])
my_unit.unit_card()