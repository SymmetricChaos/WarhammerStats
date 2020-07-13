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

my_unit.toggle_effect(effects_dict["Martial Mastery"])
my_unit.unit_card()

my_unit.toggle_effect(effects_dict["Stand Your Ground!"])
my_unit.unit_card()

my_unit.toggle_effect(effects_dict["Poison"])
my_unit.unit_card()

my_unit.set_fatigue("active")
my_unit.unit_card()

my_unit.toggle_effect(effects_dict["Martial Mastery"])
my_unit.unit_card()

my_unit.toggle_effect(effects_dict["Poison"])
my_unit.unit_card()

my_unit.set_fatigue("exhausted")
my_unit.unit_card()

my_unit.toggle_effect(effects_dict["Stand Your Ground!"])
my_unit.unit_card()





print("\n\n\nExample Ranged Unit")
sisters = TWWUnit(select_unit(unitsDF,"Sisters of Avelorn"))
sisters.unit_card()
sisters.toggle_effect(effects_dict["Loose!"])
sisters.unit_card()


slayers = TWWUnit(select_unit(unitsDF,"Giant River Troll Hag"))
slayers.unit_card()