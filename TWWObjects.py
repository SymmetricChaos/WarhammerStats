import math
import pandas as pd
import copy
import pickle
from Translators import attribute_pretty_name


fatigue_dict = pickle.load( open( "fatigueDict.p", "rb" ) )

class TWWEffect:
    
    def __init__(self,name,effects):
        self.name = name
        self.effects = effects
        
    def __str__(self):
        return f"TWWEffect: {self.name}"
    
    def __repr__(self):
        return f"TWWEffect: {self.name}"
    
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
                        if type(stat[1]) == int:
                            increase == int(increase)
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
            unit["explosion_total_damage"] = unit["explosion_base_damage"]+unit["explosion_ap_damage"]



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
        self.rank = 0
    
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
        
        # Melee Attack Stats
        melee_total = self['melee_total_damage']
        melee_base = self['melee_base_damage']
        melee_ap = self['melee_ap_damage']
        
        if self['melee_is_magical']:
            M = "M"
        else:
            M = ""
        if self['melee_is_flaming']:
            F = "F"
        else:
            F = ""
        
        weapon_strength = f"| Weapon Strength  {melee_total} ({melee_base}\\{melee_ap}) {M}{F}\n"
        
        # Armor Stats
        shield = self['missile_block_chance']
        if shield == 0:
            armor = f"| Armour           {self['armour']}\n"
        else:
            armor = f"| Armour           {self['armour']} ({shield}%)\n"
        
        spells = self['spells']
        if len(spells) == 0:
            spells = ""
        else:
            spells = f"| Spells: {', '.join(self['spells'])}\n"
        
        
        if self['ammo'] == 0:
            missile_range = ""
            missile_damage = ""
            missile_strength = ""
            ammo = ""
            
        else:
            
            if self['ranged_is_magical']:
                rM = "M"
            else:
                rM = ""
            if self['ranged_is_flaming']:
                rF = "F"
            else:
                rF = ""
            
            ranged_base = self['ranged_base_damage']
            ranged_ap = self['ranged_ap_damage']
            
            base_reload = self["base_reload_time"]
            reload_skill = self["reload_skill"]
            reload_time = base_reload*(100-reload_skill)/100
            
            ammo =             f"| Ammo             {self['ammo']} ({rM}{rF})\n"
            missile_range =    f"| Range            {self['range']}\n"
            missile_damage =   f"| Missile Damage   {self['ranged_total_damage']} ({ranged_base}\\{ranged_ap})\n"
            missile_strength = f"| Missile Strength {int(self['ranged_total_damage']*10/reload_time)} ({reload_time}s)\n"
        
        print(f"\n| {self['name']}\n|\n"
              f"| HP               {self['health']}\n"
              f"{armor}"
              f"| Leadership       {self['leadership']}\n"
              f"| Speed            {self['speed']}\n"
              f"| Melee Attack     {self['melee_attack']}\n"
              f"| Melee Defence    {self['melee_defence']}\n"
              f"{weapon_strength}"
              f"| Charge Bonus     {int(self['charge_bonus'])}\n"
              f"{ammo}"
              f"{missile_range}"
              f"{missile_strength}"
              f"{missile_damage}"
              f"|\n"
              f"| Physical Resist  {self['damage_mod_physical']}%\n"
              f"| Magic Resist     {self['damage_mod_magic']}%\n"
              f"| Flame Resist     {self['damage_mod_flame']}%\n"
              f"| Ward Save        {self['damage_mod_all']}%\n"
              f"|\n"
              f"| Fatigue: {self.fatigue.title()}\n|\n"
              f"| Attributes: {', '.join(attributes)}\n"
              f"| Abilities: {', '.join(self['abilities'])}\n"
              f"{spells}"
              f"|\n"
              f"| Active Effects: {', '.join(self.effects)}\n"
              )
        
    
    def reset_stats(self):
        self.data = self.shadow
    
    def change_stat(self,stat,value,operation,remove=False):
        if operation.lower() in ('add','addition'):
             if type(self[stat]) != str:
                 if remove == False:
                     self[stat] += value
                 else:
                     self[stat] -= value
        elif operation.lower() in ('mul','multiply','multiplication'):
             if type(self[stat]) != str:
                 increase = round(self.shadow[stat]*value-self.shadow[stat])
                 if remove == False:
                     unit[stat] += increase
                 else:
                     unit[stat] -= increase
        else:
            raise Exception("Operations must be either 'add' or 'mul'")
    
    
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
            self.fatigue = level

