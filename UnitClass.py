





if __name__ == '__main__':
    import pickle
    from UtilityFunctions import select_unit
    from EffectClass import TWWEffect
    
    unitsDF = pickle.load( open( "unitsDF.p", "rb" ) )
    stat_effects = pickle.load( open( "stat_effects.p", "rb" ) )

    my_unit = TWWUnit(select_unit(unitsDF,"Phoenix Guard"))
    
    print(my_unit)
    
    print("\nTest Bonus Vs Large")
    print("Currently it is off")
    print(my_unit.BvL_on)
    print(f"MA = {my_unit['melee_attack']}")
    print(f"Damage = {my_unit['melee_total_damage']}\n")
    
    my_unit.toggle_BvI()
    print("Toggled to on")
    print(my_unit.BvL_on)
    print(f"MA = {my_unit['melee_attack']}")
    print(f"Damage = {my_unit['melee_total_damage']}\n")
    
    my_unit.toggle_BvI()
    print("Toggled back off")
    print(my_unit.BvL_on)
    print(f"MA = {my_unit['melee_attack']}")
    print(f"Damage = {my_unit['melee_total_damage']}\n")
    
    
    
    print("\nTest Martial Mastery")
    print(my_unit.effects)
    print(f"MA = {my_unit['melee_attack']}")
    print(f"MD = {my_unit['melee_defence']}\n")
    
    my_unit.toggle_effect(stat_effects["Martial Mastery"])
    print(my_unit.effects)
    print(f"MA = {my_unit['melee_attack']}")
    print(f"MD = {my_unit['melee_defence']}\n")
    
    my_unit.toggle_effect(stat_effects["Glittering Scales"])
    print(my_unit.effects)
    print(f"MA = {my_unit['melee_attack']}")
    print(f"MD = {my_unit['melee_defence']}\n")

    my_unit.toggle_effect(stat_effects["Martial Mastery"])
    print(my_unit.effects)
    print(f"MA = {my_unit['melee_attack']}")
    print(f"MD = {my_unit['melee_defence']}")