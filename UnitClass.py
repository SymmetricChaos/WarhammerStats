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
        self.BvI = False
        self.BvL = False
        self.charge = False
        
        # names of active effects
        self.effects = []
        
        # Fatgiue level
        self.fatigue = "fresh"
    
    def __getitem__(self,n):
        return self.data[n]
    
    def __setitem__(self,n,v):
        self.data[n] = v
    
    def reset_stats(self):
        self.data = self.shadow
    
    def toggle_BvI(self):
        if self.BvI == False:
            self.BvI = True
            BvI = self.data["melee_bonus_v_infantry"]
            ap_ratio = self.shadow["melee_ap_ratio"] # note the ap ratio is pulled from shadow since only the base value matters
            self.data["melee_attack"] += BvI
            self.data["melee_base_damage"] += math.floor(BvI*(1-ap_ratio))
            self.data["melee_ap_damage"] += math.floor(BvI*(ap_ratio))
            self.data["melee_total_damage"] = self.data["melee_base_damage"]+self.data["melee_ap_damage"]
        else:
            self.BvI = False
            self.data["melee_attack"] = self.shadow["melee_attack"]
            self.data["melee_base_damage"] = self.shadow["melee_base_damage"]
            self.data["melee_ap_damage"] =self.shadow["melee_ap_damage"]
            self.data["melee_total_damage"] = self.shadow["melee_total_damage"]

    def toggle_BvL(self):
        if self.BvL == False:
            self.BvL = True
            BvL = self.data["melee_bonus_v_large"]
            ap_ratio = self.shadow["melee_ap_ratio"]
            self.data["melee_attack"] += BvL
            self.data["melee_base_damage"] += math.floor(BvL*(1-ap_ratio))
            self.data["melee_ap_damage"] += math.floor(BvL*(ap_ratio))
            self.data["melee_total_damage"] = self.data["melee_base_damage"]+self.data["melee_ap_damage"]
        else:
            self.BvL = False
            self.data["melee_attack"] = self.shadow["melee_attack"]
            self.data["melee_base_damage"] = self.shadow["melee_base_damage"]
            self.data["melee_ap_damage"] =self.shadow["melee_ap_damage"]
            self.data["melee_total_damage"] = self.shadow["melee_total_damage"]
        
    def toggle_charge(self):
        if self.charge == False:
            self.charge = True
            charge = self.data["charge_bonus"]
            ap_ratio = self.shadow["melee_ap_ratio"]
            self.data["melee_attack"] += charge
            self.data["melee_base_damage"] += math.floor(charge*(1-ap_ratio))
            self.data["melee_ap_damage"] += math.floor(charge*(ap_ratio))
            self.data["melee_total_damage"] = self.data["melee_base_damage"]+self.data["melee_ap_damage"]
        else:
            self.charge = False
            self.data["melee_attack"] = self.shadow["melee_attack"]
            self.data["melee_base_damage"] = self.shadow["melee_base_damage"]
            self.data["melee_ap_damage"] =self.shadow["melee_ap_damage"]
            self.data["melee_total_damage"] = self.shadow["melee_total_damage"]
    
    # def apply_effect(self,name):
    #     if name not in self.effects:
    #     else:





if __name__ == '__main__':
    import pickle
    from UtilityFunctions import select_unit
    
    unitsDF = pickle.load( open( "unitsDF.p", "rb" ) )
    
    my_unit = TWWUnit(select_unit(unitsDF,"Scourgerunner Chariots"))
    print(my_unit["melee_attack"])
    my_unit.toggle_BvI()
    print(my_unit["melee_attack"])
    my_unit.toggle_BvI()
    print(my_unit["melee_attack"])
    
    my_unit["abilities"].append("TEST")
    
    print(my_unit.data["abilities"])
    print(my_unit.shadow["abilities"])