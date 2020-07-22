class TWWEffect:
    
    def __init__(self,name,stat_effects,other_effects):
        self.name = name
        self.stat_effects = stat_effects
        self.other_effects = other_effects
        
    def __str__(self):
        return f"TWWEffect: {self.name}"
    
    def __repr__(self):
        return f"TWWEffect: {self.name}"
    
    @property
    def effect_card(self):
        S = f"| {self.name}\n"
        for e in self.stat_effects:
            if e[1] > 0 and e[2] == 'add':
                sign = "+"
            elif e[1] > 1 and e[2] == 'mult':
                sign = "+"
            else:
                sign = ""
            
            if e[2] == "add":
                S += f"|  {e[0]} {sign}{e[1]}\n"
            else:
                S += f"|  {e[0]} {sign}{int((e[1]-1)*100)}%\n"
        for o in self.other_effects:
            S += f"|  Grants {o}\n"
        return S
    
    def __call__(self,unit,remove=False):
        for stat, val, how in self.stat_effects:
            if 'UNUSED' in stat:
                continue
            if stat == 'speed':
                unit.change_speed(val,remove=remove)
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
        
        for imbument in self.other_effects:
            if remove == False:
                if imbument == 'imbue_magical':
                    unit['melee_is_magical'] = True
                    unit.imbue_magical += 1
                elif imbument == 'imbue_flaming':
                    unit['melee_is_flaming'] = True
                    unit.imbue_flaming += 1
                else:
                    unit['attributes'].append(imbument)
            
            else:
                if imbument == 'imbue_magical':
                    unit.imbue_magical -= 1
                    if unit.imbue_magical == 0:
                        unit['melee_is_magical'] = unit.shadow['melee_is_magical']
                elif imbument == 'imbue_flaming':
                    unit.imbue_flaming -= 1
                    if unit.imbue_flaming == 0:
                        unit['melee_is_flaming'] = unit.shadow['melee_is_flaming']
                else:
                    unit['attributes'].remove(imbument)