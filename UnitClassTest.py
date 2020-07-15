import pickle
from UtilityFunctions import select_unit
from TWWObjects import TWWUnit

effects_dict = pickle.load( open( "effectsDict.p", "rb" ) )
unitsDF = pickle.load( open( "unitsDF.p", "rb" ) )

my_unit = TWWUnit(select_unit(unitsDF,"Phoenix Guard"))

print("\nTest Bonus Vs Large")
my_unit.unit_card()

my_unit.toggle_BvL()
my_unit.unit_card()

my_unit.toggle_BvL()
my_unit.unit_card()




print("\n\n\nTest Effects")

my_unit.toggle_effect("Martial Mastery")
my_unit.unit_card()

my_unit.toggle_effect("Stand Your Ground!")
my_unit.unit_card()

my_unit.toggle_effect("Poison!")
my_unit.unit_card()

my_unit.set_fatigue("active")
my_unit.unit_card()

my_unit.toggle_effect("Martial Mastery")
my_unit.unit_card()

my_unit.toggle_effect("Poisoned")
my_unit.unit_card()

my_unit.set_fatigue("exhausted")
my_unit.unit_card()

my_unit.toggle_effect("Stand Your Ground!")
my_unit.unit_card()





print("\n\n\nExample Ranged Unit")
ranged = TWWUnit(select_unit(unitsDF,"Darkshards"))
ranged.unit_card()

print("\n\n\nExample Unit With Lots of Attributes, Abilities, and Spells")
lots_of_lists = TWWUnit(select_unit(unitsDF,"Settra the Imperishable"))
lots_of_lists.unit_card()