import pickle
from TWWObjects import TWWUnit
from UtilityFunctions import select_unit

unitsDF = pickle.load( open( "unitsDF.p", "rb" ) )

print("\nTest Bonus Vs Large")
my_unit = TWWUnit(select_unit(unitsDF,"Phoenix Guard"))
print(my_unit.unit_card)

my_unit.toggle_BvL()
print(my_unit.unit_card)

my_unit.toggle_BvL()
print(my_unit.unit_card)



print("\n\n\nTest Effects")
my_unit.toggle_effect("Martial Mastery")
print(my_unit.unit_card)

my_unit.toggle_effect("Stand Your Ground!")
print(my_unit.unit_card)

my_unit.toggle_effect("Poison!")
print(my_unit.unit_card)

my_unit.set_fatigue("active")
print(my_unit.unit_card)

my_unit.toggle_effect("Martial Mastery")
print(my_unit.unit_card)

my_unit.toggle_effect("Poison!")
print(my_unit.unit_card)

my_unit.set_fatigue("exhausted")
print(my_unit.unit_card)

my_unit.toggle_effect("Stand Your Ground!")
print(my_unit.unit_card)



print("\n\n\nExample Ranged Unit")
ranged = TWWUnit(select_unit(unitsDF,"Queen Bess"))
print(ranged.unit_card)



print("\n\n\nExample Unit With Lots of Attributes, Abilities, and Spells")
lots_of_lists = TWWUnit(select_unit(unitsDF,"Settra the Imperishable on Chariot of the Gods"))
print(lots_of_lists.unit_card)



print("\n\n\nExample of Fatigue")
fatigue_example = TWWUnit(select_unit(unitsDF,"Swordsmen"))
print(fatigue_example.unit_card)

fatigue_example.set_fatigue("Exhausted")
print(fatigue_example.unit_card)

fatigue_example.set_fatigue("fresh")
print(fatigue_example.unit_card)



print("\n\n\nExample of Rank")
rank_example = TWWUnit(select_unit(unitsDF,"Flagellants"))
print(rank_example.unit_card)

rank_example.set_rank(9)
print(rank_example.unit_card)



print("\n\n\nExample of Speed")
flier = TWWUnit(select_unit(unitsDF,"Feral Wyvern"))
print(flier['run_speed'])
print(flier['fly_speed'])
print(flier['charge_speed'])
print(flier['charge_speed_flying'])
flier.toggle_effect("Frostbite!")
print(flier['run_speed'])
print(flier['fly_speed'])
print(flier['charge_speed'])
print(flier['charge_speed_flying'])



print("\n\n\nExample of Imbuments")
imbument_example = TWWUnit(select_unit(unitsDF,"Grail Knights"))
print(imbument_example.unit_card)
imbument_example.toggle_effect("Flaming Sword of Rhuin")
print(imbument_example.unit_card)
imbument_example.toggle_effect("Flaming Sword of Rhuin")
print(imbument_example.unit_card)