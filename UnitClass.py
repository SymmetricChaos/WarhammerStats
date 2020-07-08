import math
import pandas as pd
import copy

class TWWUnit:
    
    def __init__(self,data):
        if type(data) != pd.core.series.Series:
            raise Exception("data must be a Pandas Series object."
                            " The select_unit() function from Utility Functions "
                            "will return this kind of object")
        self.data = dict(data)
        self.shadow = copy.deepcopy(dict(data)) # shadow not to be modified
        
        # Toggleable stats
        self.BvI_on = False
        self.BvL_on = False
        self.charge_on = False
        
        # names of active effects
        self.effects = []
        
        # Fatgiue level
        self.fatigue = "fresh"
    
    def __getitem__(self,n):
        return self.data[n]
    
    def __setitem__(self,n,v):
        self.data[n] = v
        
    def __str__(self):
        return f"TWWUnit: {self['name']}"
    
    def reset_stats(self):
        self.data = self.shadow
    
    def toggle_BvI(self):
        BvI = self.data["melee_bonus_v_infantry"]
        ap_ratio = self.shadow["melee_ap_ratio"] # note the ap ratio is pulled from shadow since only the base value matters
        if self.BvI_on == False:
            self.BvI_on = True
            self.data["melee_attack"] += BvI
            self.data["melee_base_damage"] += math.floor(BvI*(1-ap_ratio))
            self.data["melee_ap_damage"] += math.floor(BvI*(ap_ratio))
            self.data["melee_total_damage"] = self.data["melee_base_damage"]+self.data["melee_ap_damage"]
        else:
            self.BvI_on = False
            self.data["melee_attack"] -= BvI
            self.data["melee_base_damage"] -= math.floor(BvI*(1-ap_ratio))
            self.data["melee_ap_damage"] -= math.floor(BvI*(ap_ratio))
            self.data["melee_total_damage"] = self.data["melee_base_damage"]+self.data["melee_ap_damage"]

    def toggle_BvL(self):
        BvL = self.data["melee_bonus_v_large"]
        ap_ratio = self.shadow["melee_ap_ratio"]
        if self.BvL_on == False:
            self.BvL_on = True
            self.data["melee_attack"] += BvL
            self.data["melee_base_damage"] += math.floor(BvL*(1-ap_ratio))
            self.data["melee_ap_damage"] += math.floor(BvL*(ap_ratio))
            self.data["melee_total_damage"] = self.data["melee_base_damage"]+self.data["melee_ap_damage"]
        else:
            self.BvL_on = False
            self.data["melee_attack"] -= BvL
            self.data["melee_base_damage"] -= math.floor(BvL*(1-ap_ratio))
            self.data["melee_ap_damage"] -= math.floor(BvL*(ap_ratio))
            self.data["melee_total_damage"] = self.data["melee_base_damage"]+self.data["melee_ap_damage"]
        
    def toggle_charge(self):
        charge = self.data["charge_bonus"]
        ap_ratio = self.shadow["melee_ap_ratio"]
        if self.charge_on == False:
            self.charge_on = True
            self.data["melee_attack"] += charge
            self.data["melee_base_damage"] += math.floor(charge*(1-ap_ratio))
            self.data["melee_ap_damage"] += math.floor(charge*(ap_ratio))
            self.data["melee_total_damage"] = self.data["melee_base_damage"]+self.data["melee_ap_damage"]
        else:
            self.charge_on = False
            self.data["melee_attack"] -= charge
            self.data["melee_base_damage"] -= math.floor(charge*(1-ap_ratio))
            self.data["melee_ap_damage"] -= math.floor(charge*(ap_ratio))
            self.data["melee_total_damage"] = self.data["melee_base_damage"]+self.data["melee_ap_damage"]
    
    def toggle_effect(self,effect):
        if effect not in self.effects:
            self.effects.append(effect)
            effect(self)
        else:
            for n,e in enumerate(self.effects):
                if e == effect:
                    break
            del self.effects[n]
            effect(self,remove=True)





if __name__ == '__main__':
    import pickle
    from UtilityFunctions import select_unit
    from EffectClass import TWWEffect
    
    unitsDF = pickle.load( open( "unitsDF.p", "rb" ) )
    stat_effects = pickle.load( open( "stat_effects.p", "rb" ) )

    my_unit = TWWUnit(select_unit(unitsDF,"Scourgerunner Chariots"))
    
    print(my_unit)
    
    print("\nTest Bonus Vs Infantry")
    print("Currently it is off")
    print(my_unit.BvI_on)
    print(f"MA = {my_unit['melee_attack']}\n")
    
    my_unit.toggle_BvI()
    print("Toggled to on")
    print(my_unit.BvI_on)
    print(f"MA = {my_unit['melee_attack']}\n")
    
    my_unit.toggle_BvI()
    print("Toggled back off")
    print(my_unit.BvI_on)
    print(f"MA = {my_unit['melee_attack']}\n")
    

    
    my_unit["abilities"].append("TEST")
    
    print(my_unit["abilities"])
    print(my_unit.shadow["abilities"])
    
    print(my_unit["melee_defence"])
    my_unit.toggle_effect(stat_effects["Stand Your Ground"])
    print(my_unit.effects)
    print(my_unit["melee_defence"])
    my_unit.toggle_effect(stat_effects["Stand Your Ground"])
    print(my_unit.effects)
    print(my_unit["melee_defence"])