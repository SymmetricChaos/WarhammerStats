import math
import pandas as pd
import copy
import pickle
import textwrap
from Translators import faction_code_to_name


class TWWEffect:
    
    def __init__(self,name,stat_effects,other_effects):
        self.name = name
        self.stat_effects = stat_effects
        self.other_effects = other_effects
        
    def __str__(self):
        return f"TWWEffect: {self.name}"
    
    def __repr__(self):
        return f"TWWEffect: {self.name}"
    
    def display(self):
        return f"{self.name}\n{self.stat_effects}\n{self.other_effects}"
    
    # This needs to deal with the fact that "speed" affects several stats
    def __call__(self,unit,remove=False):
        if type(unit) != TWWUnit:
            raise Exception(f"Input must be of type TWWUnit not {type(unit)}")
        for stat, val, how in self.stat_effects:
            if 'UNUSED' in stat:
                continue
            if stat == 'speed':
                if remove == False:
                    unit.change_speed(val)
                else:
                     unit.change_speed(val,remove=True)
            else:
                if how == 'mult':
                    increase = round(unit.shadow[stat]*val-unit.shadow[stat])
                    if type(stat) == int:
                        increase == int(increase)
                    if remove == False:
                        unit[stat] += increase
                    else:
                        unit[stat] -= increase
            
                elif how == 'add':
                    if remove == False:
                        unit[stat] += val
                    else:
                        unit[stat] -= val
            
            
            unit["melee_total_damage"] = unit["melee_base_damage"]+unit["melee_ap_damage"]
            unit["ranged_total_damage"] = unit["ranged_base_damage"]+unit["ranged_ap_damage"]
            unit["explosion_total_damage"] = unit["explosion_base_damage"]+unit["explosion_ap_damage"]


effects_dict = pickle.load( open( "effectsDict.p", "rb" ) )
fatigue_dict = pickle.load( open( "fatigueDict.p", "rb" ) )


class TWWUnit:
    
    # This is a large dictionary but it is very use to have it be part of the
    # definition of TWWUnit. As an class variable it is stored only once even
    # if multiple TWWUnit objects exist
    EFFECTS = effects_dict
    FATIGUE = fatigue_dict
    EXP = {'accuracy': [0,3],
            'melee_attack': [0.6,0.12],
            'melee_defence': [0.6,0.12],
            'leadership': [0,1.06],
            'reload_skill': [0,1.8],
            }
    FACTION = faction_code_to_name
    
    def __init__(self,data):
        if type(data) != pd.core.series.Series:
            raise Exception("data must be a Pandas Series object."
                            " The select_unit() function from Utility Functions "
                            "will return this kind of object")
        self.data = dict(data)
        self.shadow = copy.deepcopy(dict(data)) # shadow not to be modified
        
        # names of active effects
        self.effects = []
    
    def __getitem__(self,n):
        return self.data[n]
    
    def __setitem__(self,n,v):
        self.data[n] = v
    
    def __str__(self):
        return f"TWWUnit: {self['name']} ({self['faction']})"
    
    def __repr__(self):
        return str(self)
    
    def melee_stat_block(self):
        stat_block = ""
        
        # HP and Armor
        stat_block += f"| HP               {self['health']}\n"
        stat_block += f"| Armour           {self['armour']}"
        
        if self['missile_block_chance'] != 0:
            stat_block += f" ({self['missile_block_chance']}%)\n"
        else:
            stat_block += "\n"
        
        # Leadership
        stat_block += f"| Leadership       {self['leadership']}\n"
        stat_block += f"| Speed            {self['speed']}\n"
        
        # Melee Attack
        stat_block += f"| Melee Attack     {self['melee_attack']}"
        if self['melee_is_magical']:
            stat_block += " M"
        if self['melee_is_flaming']:
            stat_block += " F"
        if self['melee_contact_effect'] != "":
            stat_block += f" ({self['melee_contact_effect']})"
        stat_block += "\n"
        
        # Melee Defence
        stat_block += f"| Melee Defence    {self['melee_defence']}\n"
        
        # Weapon Strength
        melee_total = self['melee_total_damage']
        melee_base = self['melee_base_damage']
        melee_ap = self['melee_ap_damage']
        
        stat_block += f"| Weapon Strength  {melee_total} ({melee_base}\\{melee_ap})"
        
        if self['melee_bonus_v_large'] != 0:
            stat_block += f" BvL:{self['melee_bonus_v_large']}"
        if self['melee_bonus_v_infantry'] != 0:
            stat_block += f" BvI:{self['melee_bonus_v_infantry']}"
        stat_block += "\n"
        
        #Charge Bonus
        stat_block += f"| Charge Bonus     {self['charge_bonus']}\n"
        
        return stat_block
    
    def ranged_stat_block(self):
        stat_block = ""
        # Empty for units with no ammo
        if self['ammo'] == 0:
            return stat_block
        
        # Ammo line
        stat_block += f"| Ammo             {self['ammo']}"
        
        if self['ranged_is_magical']:
            stat_block += "M"
        if self['ranged_is_flaming']:
            stat_block += "F"
        stat_block += "\n"
        
        # Range
        stat_block +=    f"| Range            {self['range']}\n"
        
        # Very complex missile strength line, needs to match in game line
        ranged_base = self['ranged_base_damage']
        ranged_ap = self['ranged_ap_damage']
        
        base_reload = self["base_reload_time"]
        reload_skill = self["reload_skill"]
        reload_time = base_reload*(100-reload_skill)/100
        num_proj = self['projectile_number']
        shots_vol = self['shots_per_volley']
        stat_block += f"| Missile Strength {int(self['ranged_total_damage']*10/reload_time*num_proj*shots_vol)} ({reload_time}s)"
        if self['ranged_bonus_v_large'] != 0:
            stat_block += f" BvL:{self['ranged_bonus_v_large']}"
        if self['ranged_bonus_v_infantry'] != 0:
            stat_block += f" BvI:{self['ranged_bonus_v_infantry']}"
        if self['ranged_contact_effect'] != "":
            stat_block += f" {self['ranged_contact_effect']}"
        stat_block += "\n"
        
        # Exact info about missile damage
        if num_proj == 1 and shots_vol == 1:
            proj_mul = ""
        else:
            proj_mul = f"×{num_proj*shots_vol}"
        stat_block +=   f"| Missile Damage   {self['ranged_total_damage']}{proj_mul} ({ranged_base}\\{ranged_ap})\n"
        
        if self['explosion_total_damage'] != 0:
            stat_block +=   f"| Explosion Damage {self['explosion_total_damage']} ({self['explosion_base_damage']}\\{self['explosion_ap_damage']})\n"
        
        return stat_block
    
    def resistances_stat_block(self):
        if sum([self['damage_mod_physical'],self['damage_mod_magic'],self['damage_mod_missile'],
               self['damage_mod_flame'],self['damage_mod_all']]) == 0:
            return ""
        else:
            stat_block = "|\n"
            if self['damage_mod_physical'] != 0:
                stat_block += f"| Physical Resist  {self['damage_mod_physical']}%\n"
            if self['damage_mod_magic'] != 0:
                stat_block += f"| Magic Resist     {self['damage_mod_magic']}%\n"
            if self['damage_mod_missile'] != 0:
                stat_block += f"| Missile Resist   {self['damage_mod_missile']}%\n"
            if self['damage_mod_flame'] != 0:
                stat_block += f"| Flame Resist     {self['damage_mod_flame']}%\n"
            if self['damage_mod_all'] != 0:
                stat_block += f"| Ward Save        {self['damage_mod_all']}%\n"
        return stat_block
    
    
    @property
    def unit_card(self):
        
        
        ### Spells, Attributes, Abilities ###
        spells = self['spells']
        if len(spells) == 0:
            spells = ""
        else:
            spells = textwrap.wrap(f"| Spells: {', '.join(self['spells'])}",45)
            spells = "\n|    ".join(spells) + "\n"
        
        attributes = textwrap.wrap(f"| Attributes: {', '.join(self['attributes'])}",45)
        attributes = "\n|    ".join(attributes)
        
        abilities = textwrap.wrap(f"| Abilities: {', '.join(self['abilities'])}",45)
        abilities = "\n|    ".join(abilities)
        
        active_effects = self.effects
        if len(active_effects) == 0:
            active_effects = "| Active Effects: None"
        else:
            active_effects = textwrap.wrap(f"| Active Effects: {', '.join(active_effects)}",45)
            active_effects = "\n|    ".join(active_effects) + "\n"
        
        
        # Lords and heroes always have the same unit count and rank
        if self['caste'] not in ('Lord','Hero'):
            units = f"| Units: {self['unit_size']}\n"
            rank = f"| Rank: {self['rank']}\n"
        else:
            units = ""
            rank = ""
        
        ### Giant String ###
        return f"\n| {self['name']} ({self['faction']})\n" \
               f"| {self['category']}\n" \
               f"{units}" \
               f"{rank}" \
               f"|\n" \
               f"{self.melee_stat_block()}" \
               f"{self.ranged_stat_block()}" \
               f"{self.resistances_stat_block()}" \
               f"|\n" \
               f"| Fatigue: {self['fatigue'].title()}\n" \
               f"|\n" \
               f"{attributes}\n" \
               f"{abilities}\n" \
               f"{spells}" \
               f"|\n" \
               f"{active_effects}\n"
    
    
    # Completely reset the units stats
    def reset_unit(self):
        self.data = self.shadow
    
    # Reset a specific stat
    def reset_stat(self,stat):
        self.data[stat] = self.shadow[stat]
    
    
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
                     self[stat] += increase
                 else:
                     self[stat] -= increase
        else:
            raise Exception("Operations must be either 'add' or 'mul'")
    
    
    # Need this because there are so many different speeds
    def change_speed(self,value,remove=False):
        for speed_type in ('speed','run_speed','fly_speed','charge_speed','charge_speed_flying'):
            increase = round(self.shadow[speed_type]*value-self.shadow[speed_type])
            if remove == False:
                self[speed_type] += increase
            else:
                self[speed_type] -= increase
    
    
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
        if effect not in self.effects:
            self.effects.append(effect)
            self.EFFECTS[effect](self)
        else:
            self.effects.remove(effect)
            self.EFFECTS[effect](self,remove=True)
    
    def set_fatigue(self,level):
        level = level.lower()
        if self['fatigue'] == level:
            return None
        else:
            # Reset fatigue first
            for stat in ("melee_attack","melee_defence","melee_ap_damage","armour","charge_bonus"):
                mul = self.FATIGUE[self['fatigue']][stat]
                increase = round(self.shadow[stat]*mul-self.shadow[stat])
                self[stat] -= increase
            
            # Then apply fatigue
            for stat in ("melee_attack","melee_defence","melee_ap_damage","armour","charge_bonus"):
                mul = self.FATIGUE[level][stat]
                increase = round(self.shadow[stat]*mul-self.shadow[stat])
                self[stat] += increase
            self.data["melee_total_damage"] = self.data["melee_base_damage"]+self.data["melee_ap_damage"]
            self['fatigue'] = level
    
    # this is weirdly complicated?
    # reload and leadership work correctly, accuracy probably does
    # unclear on how melee attack and melee defence work
    def set_rank(self,level):
        if level not in (0,1,2,3,4,5,6,7,8,9):
            raise Exception("Rank must be an integer from 0 to 9")
        if self['caste'] in ('Lord','Hero'):
            raise Exception("Characters do not gain unit ranks (chevrons).")
        if self['rank'] == level:
            return None
        else:
            # Reset rank
            for stat,val in self.EXP.items():
                change = round(val[1]*self['rank'])
                self[stat] -= change
        
            # Then apply rank
            for stat,val in self.EXP.items():
                change = round(val[1]*level)
                self[stat] += change
            self['rank'] = level