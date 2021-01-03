import pickle
from TWWObjects import TWWUnit
from UtilityFunctions import select_unit

unitsDF = pickle.load( open( "DataFiles\\unitsDF.p", "rb" ) )

def check_BvL():
    print("\nTest Bonus Vs Large")
    my_unit = TWWUnit(select_unit(unitsDF,"Phoenix Guard"))
    print(my_unit.unit_card)
    my_unit.toggle_BvL()
    print(my_unit.unit_card)
    my_unit.toggle_BvL()
    print(my_unit.unit_card)


def check_effects():
    print("\n\n\nTest Effects")
    my_unit = TWWUnit(select_unit(unitsDF,"Phoenix Guard"))
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


def check_ranged():
    print("\n\n\nExample Ranged Unit")
    ranged = TWWUnit(select_unit(unitsDF,"Queen Bess"))
    print(ranged.unit_card)


def check_linebreaking():
    print("\n\n\nExample Unit With Lots of Attributes, Abilities, and Spells")
    lots_of_lists = TWWUnit(select_unit(unitsDF,"Settra the Imperishable on Chariot of the Gods"))
    print(lots_of_lists.unit_card)


def check_fatigue():
    print("\n\n\nExample of Fatigue")
    fatigue_example = TWWUnit(select_unit(unitsDF,"Swordsmen"))
    print(fatigue_example.unit_card)
    fatigue_example.set_fatigue("Exhausted")
    print(fatigue_example.unit_card)
    fatigue_example.set_fatigue("fresh")
    print(fatigue_example.unit_card)


def check_rank():
    print("\n\n\nExample of Rank")
    rank_example = TWWUnit(select_unit(unitsDF,"wh2_main_hef_inf_archers_0"))
    print(rank_example.unit_card)
    rank_example.set_rank(9)
    print(rank_example.unit_card)
    rank_example.set_rank(0)
    print(rank_example.unit_card)


def check_speed():
    print("\n\n\nExample of Speed")
    flier = TWWUnit(select_unit(unitsDF,"wh2_main_hef_mon_great_eagle"))
    print(flier.unit_card)
    print(flier.speeds)
    flier.toggle_effect("Frostbite!")
    print(flier.unit_card)
    print(flier.speeds)


def check_imbuments():
    print("\n\n\nExample of Imbuments")
    imbument_example = TWWUnit(select_unit(unitsDF,"Sisters of Avelorn"))
    print(imbument_example.unit_card)
    imbument_example.toggle_effect("Flaming Sword of Rhuin")
    print(imbument_example.unit_card)
    imbument_example.toggle_effect("Flaming Sword of Rhuin")
    print(imbument_example.unit_card)


def check_technology():
    print("\n\n\nExample of Technology")
    tech_example = TWWUnit(select_unit(unitsDF,"wh2_main_hef_mon_great_eagle"))
    print(tech_example.unit_card)
    tech_example.toggle_technology("Swiftsense")
    tech_example.toggle_technology("Heavy Ithilmar Armour")
    print(tech_example.unit_card)
    
    tech_example = TWWUnit(select_unit(unitsDF,"Phoenix Guard"))
    print(tech_example.unit_card)
    tech_example.toggle_technology("Swiftsense")
    tech_example.toggle_technology("Heavy Ithilmar Armour")
    print(tech_example.unit_card)





if __name__ == '__main__':
    check_technology()