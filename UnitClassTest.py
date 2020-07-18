import pickle
from UtilityFunctions import select_unit
from TWWObjects import TWWUnit

effects_dict = pickle.load( open( "effectsDict.p", "rb" ) )
unitsDF = pickle.load( open( "unitsDF.p", "rb" ) )


# print("\nTest Bonus Vs Large")

# my_unit = TWWUnit(select_unit(unitsDF,"Phoenix Guard"))
# print(my_unit.unit_card)

# my_unit.toggle_BvL()
# print(my_unit.unit_card)

# my_unit.toggle_BvL()
# print(my_unit.unit_card)



# print("\n\n\nTest Effects")

# my_unit.toggle_effect("Martial Mastery")
# print(my_unit.unit_card)

# my_unit.toggle_effect("Stand Your Ground!")
# print(my_unit.unit_card)

# my_unit.toggle_effect("Poison!")
# print(my_unit.unit_card)

# my_unit.set_fatigue("active")
# print(my_unit.unit_card)

# my_unit.toggle_effect("Martial Mastery")
# print(my_unit.unit_card)

# my_unit.toggle_effect("Poison!")
# print(my_unit.unit_card)

# my_unit.set_fatigue("exhausted")
# print(my_unit.unit_card)

# my_unit.toggle_effect("Stand Your Ground!")
# print(my_unit.unit_card)





print("\n\n\nExample Ranged Unit")
ranged = TWWUnit(select_unit(unitsDF,"Queen Bess"))
print(ranged.unit_card)

# print("\n\n\nExample Unit With Lots of Attributes, Abilities, and Spells")
# lots_of_lists = TWWUnit(select_unit(unitsDF,"Settra the Imperishable on Chariot of the Gods"))
# print(lots_of_lists.unit_card)


# print("\n\n\nExample of Fatigue")
# fatigue_example = TWWUnit(select_unit(unitsDF,"Swordsmen"))
# print(fatigue_example.unit_card)
# fatigue_example.set_fatigue("Exhausted")
# print(fatigue_example.unit_card)
# fatigue_example.set_fatigue("fresh")
# print(fatigue_example.unit_card)


# print("\n\n\nExample of Rank")
# rank_example = TWWUnit(select_unit(unitsDF,"Black Lions"))
# print(rank_example.unit_card)
# rank_example.set_rank(9)
# print(rank_example.unit_card)

print("\n\n\nTest Different Combinations of Stat Blocks")
print(TWWUnit(select_unit(unitsDF,"Queen Bess")).unit_card)
print(TWWUnit(select_unit(unitsDF,"Crossbowmen")).unit_card)
print(TWWUnit(select_unit(unitsDF,"Casket of Souls")).unit_card)
print(TWWUnit(select_unit(unitsDF,"Chosen")).unit_card)