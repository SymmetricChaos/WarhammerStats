import math
import pandas as pd
import copy
import pickle
from Translators import attribute_pretty_name


fatigue_dict = pickle.load( open( "fatigueDict.p", "rb" ) )

class TWWEffect:
    
    def __init__(self,name,effects):
        self.name = name
        self.pretty_name = name
        if self.pretty_name == "":
            self.pretty_name = " ".join(name.split("_")[3:]).title()
        self.effects = effects
        
    def __str__(self):
        return f"TWWEffect: {self.pretty_name}"
    
    def __repr__(self):
        return f"TWWEffect: {self.pretty_name}"
    
    # This needs to deal with the fact that "speed" affects several stats
    def __call__(self,unit,remove=False):
        if type(unit) != TWWUnit:
            raise Exception(f"Input must be of type TWWUnit not {type(unit)}")
        for stat in self.effects:
            if 'UNUSED' in stat[1]:
                continue
            else:
                if stat[2] == 'mult':
                    try:
                        increase = round(unit.shadow[stat[1]]*stat[0]-unit.shadow[stat[1]])
                        if remove == False:
                            unit[stat[1]] += increase
                        else:
                            unit[stat[1]] -= increase
                    except:
                        pass
                elif stat[2] == 'add':
                    try:
                        if remove == False:
                            unit[stat[1]] += stat[0]
                        else:
                            unit[stat[1]] -= stat[0]
                    except:
                        pass
            unit["melee_total_damage"] = unit["melee_base_damage"]+unit["melee_ap_damage"]
            unit["ranged_total_damage"] = unit["ranged_base_damage"]+unit["ranged_ap_damage"]



class TWWUnit:
    
    def __init__(self,data):
        if type(data) != pd.core.series.Series:
            raise Exception("data must be a Pandas Series object."
                            " The select_unit() function from Utility Functions "
                            "will return this kind of object")
        self.data = dict(data)
        self.shadow = copy.deepcopy(dict(data)) # shadow not to be modified
        
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
    
    def __repr__(self):
        return f"TWWUnit: {self['name']}"
    
    def unit_card(self):
        attributes = [attribute_pretty_name[att] for att in self['attributes']]
        
        melee_total = int(self['melee_total_damage'])
        melee_base = int(self['melee_base_damage'])
        melee_ap = int(self['melee_ap_damage'])
        
        if self['melee_is_magical']:
            M = "M"
        else:
            M = ""
        if self['melee_is_flaming']:
            F = "F"
        else:
            F = ""
        
        if math.isnan(self['ammo']):
            ammo = ""
        else:
            ammo = f"| Ammo             {int(self['ammo'])}\n"
        
        if math.isnan(self['range']):
            weapon_range = ""
        else:
            weapon_range = f"| Range            {int(self['range'])}\n"
            
        if math.isnan(self['ranged_total_damage']):
            missile = ""
        else:
            missile = f"| Missile Strength {int(self['ranged_total_damage'])}\n"
        
        
        # NEED TO UPDATE WITH RANGED INFO
        
        print(f"\n| {self['name']}\n|\n"
              f"| HP               {self['health']}\n"
              f"| Armour           {int(self['armour'])}\n"
              f"| Leadership       {int(self['leadership'])}\n"
              f"| Speed            {int(self['speed'])}\n"
              f"| Melee Attack     {int(self['melee_attack'])}\n"
              f"| Melee Defence    {int(self['melee_defence'])}\n"
              f"| Weapon Strength  {melee_total} ({melee_base}\\{melee_ap}) {M}{F}\n"
              f"| Charge Bonus     {int(self['charge_bonus'])}\n"
              f"{ammo}"
              f"{weapon_range}"
              f"{missile}"
              f"|\n"
              f"| phys_res         {self['damage_mod_physical']}%\n"
              f"| mag_res          {self['damage_mod_magic']}%\n"
              f"| fire_res         {self['damage_mod_flame']}%\n"
              f"| ward_res         {self['damage_mod_all']}%\n|\n"
              f"| Attributes: {', '.join(attributes)}\n"
              f"| Abilities: {', '.join(self['abilities'])}\n|\n"
              f"| Active Effects: {', '.join(self.effects)}\n"
              )
        
    
    def reset_stats(self):
        self.data = self.shadow
    
    def toggle_BvI(self):
        BvI = self.data["melee_bonus_v_infantry"]
        ap_ratio = self.shadow["melee_ap_ratio"] # note the ap ratio is pulled from shadow since only the base value matters
        if "BvI" not in self.effects:
            self.effects.append("BvI")
            self.data["melee_attack"] += BvI
            self.data["melee_base_damage"] += math.floor(BvI*(1-ap_ratio))
            self.data["melee_ap_damage"] += math.floor(BvI*(ap_ratio))
            self.data["melee_total_damage"] = self.data["melee_base_damage"]+self.data["melee_ap_damage"]
        else:
            self.effects.remove("BvI")
            self.data["melee_attack"] -= BvI
            self.data["melee_base_damage"] -= math.floor(BvI*(1-ap_ratio))
            self.data["melee_ap_damage"] -= math.floor(BvI*(ap_ratio))
            self.data["melee_total_damage"] = self.data["melee_base_damage"]+self.data["melee_ap_damage"]
    
    def toggle_BvL(self):
        BvL = self.data["melee_bonus_v_large"]
        ap_ratio = self.shadow["melee_ap_ratio"]
        if "BvL" not in self.effects:
            self.effects.append("BvL")
            self.data["melee_attack"] += BvL
            self.data["melee_base_damage"] += math.floor(BvL*(1-ap_ratio))
            self.data["melee_ap_damage"] += math.floor(BvL*(ap_ratio))
            self.data["melee_total_damage"] = self.data["melee_base_damage"]+self.data["melee_ap_damage"]
        else:
            self.effects.remove("BvL")
            self.data["melee_attack"] -= BvL
            self.data["melee_base_damage"] -= math.floor(BvL*(1-ap_ratio))
            self.data["melee_ap_damage"] -= math.floor(BvL*(ap_ratio))
            self.data["melee_total_damage"] = self.data["melee_base_damage"]+self.data["melee_ap_damage"]
    
    def toggle_charge(self):
        charge = self.data["charge_bonus"]
        ap_ratio = self.shadow["melee_ap_ratio"]
        if "Charge Bonus" not in self.effects:
            self.effects.append("Charge Bonus")
            self.data["melee_attack"] += charge
            self.data["melee_base_damage"] += math.floor(charge*(1-ap_ratio))
            self.data["melee_ap_damage"] += math.floor(charge*(ap_ratio))
            self.data["melee_total_damage"] = self.data["melee_base_damage"]+self.data["melee_ap_damage"]
        else:
            self.effects.remove("Charge Bonus")
            self.data["melee_attack"] -= charge
            self.data["melee_base_damage"] -= math.floor(charge*(1-ap_ratio))
            self.data["melee_ap_damage"] -= math.floor(charge*(ap_ratio))
            self.data["melee_total_damage"] = self.data["melee_base_damage"]+self.data["melee_ap_damage"]
    
    def toggle_effect(self,effect):
        if effect.pretty_name not in self.effects:
            self.effects.append(effect.pretty_name)
            effect(self)
        else:
            self.effects.remove(effect.pretty_name)
            effect(self,remove=True)
    
    def set_fatigue(self,level):
        if self.fatigue == level:
            return None
        else:
            # Reset fatigue first
            for stat in ("melee_attack","melee_defence","melee_ap_damage","armour","charge_bonus"):
                mul = fatigue_dict[self.fatigue][stat]
                increase = round(self.shadow[stat]*mul-self.shadow[stat])
                self[stat] += increase
            
            # Then apply fatigue
            for stat in ("melee_attack","melee_defence","melee_ap_damage","armour","charge_bonus"):
                mul = fatigue_dict[level][stat]
                increase = round(self.shadow[stat]*mul-self.shadow[stat])
                self[stat] += increase
            self.data["melee_total_damage"] = self.data["melee_base_damage"]+self.data["melee_ap_damage"]

