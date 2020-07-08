import csv
import math

class TWWEffect:
    
    def __init__(self,name,effects):
        self.name = name
        self.pretty_name = " ".join(name.split("_")[4:]).title()
        if self.pretty_name == "":
            self.pretty_name = " ".join(name.split("_")[3:]).title()
        self.effects = effects
        
    def __str__(self):
        return self.pretty_name
    
    def __repr__(self):
        return self.pretty_name
    
    def __call__(self,unit,remove=False):
        for stat in self.effect:
            if 'UNUSED' in stat[1]:
                continue
            else:
                if stat[2] == 'mult':
                    increase = math.floor(unit.shadow[stat[1]]*stat[0])-unit.shadow[stat[1]]
                    if remove == False:
                        unit[stat[1]] += increase
                    else:
                        unit[stat[1]] -= increase
                elif stat[2] == 'add':
                    if remove == False:
                        unit[stat[1]] += stat[0]
                    else:
                        unit[stat[1]] -= stat[0]
                else:
                    raise Exception(f"{self.pretty_name} uses the {stat[2]} to modify a stat")




# Translate stats to names used in the unitsDF
stat_translator = {
                    'stat_reloading': 'reload_skill',
                   
                    'scalar_missile_explosion_damage_base': 'explosion_base_damage',
                    'scalar_missile_explosion_damage_ap': 'explosion_ap_damage',
                   
                    
                    
                    'stat_melee_damage_base': 'melee_base_damage', 
                    'stat_melee_damage_ap': 'melee_ap_damage',
                   
                    'scalar_missile_damage_ap': 'ranged_ap_damage',
                    'scalar_missile_damage_base': 'ranged_base_damage',
                    'scalar_missile_range': 'range',
                   
                    'scalar_speed': 'speed', # note multiple speed
                    'scalar_charge_speed': 'charge_speed',
                    'stat_charge_bonus': 'charge_bonus', # note multiple charge speeds, too
                   
                    'stat_accuracy': 'UNUSED_stat_accuracy',
                    'scalar_entity_acceleration_modifier': 'UNUSED_scalar_entity_acceleration_modifier',
                    'scalar_entity_deceleration_modifier':  'UNUSED_scalar_entity_deceleration_modifier',
                    'scalar_dealt_collision_knocked_down_threshold_modifier': 'UNUSED_scalar_dealt_collision_knocked_down_threshold_modifier',
                    'scalar_dealt_collision_knocked_flying_threshold_modifier': 'UNUSED_scalar_dealt_collision_knocked_flying_threshold_modifier',
                    'scalar_dealt_collision_knocked_back_threshold_modifier': 'UNUSED_scalar_dealt_collision_knocked_back_threshold_modifier',
                    'scalar_bracing': 'UNUSED_scalar_bracing',
                    'scalar_miscast_chance': 'UNUSED_scalar_miscast_chance', # currently unused, add this?
                    'scalar_splash_attack_power': 'UNUSED_scalar_splash_attack_power',
                   
                    'stat_bonus_vs_large': 'melee_bonus_v_large',
                    'stat_bonus_vs_infantry': 'melee_bonus_v_infantry',
                   
                    'stat_morale': 'leadership',
                   
                    'stat_resistance_all': 'damage_mod_all',
                    'stat_resistance_missile': 'damage_mod_missile',
                    'stat_resistance_flame': 'damage_mod_flame',
                    'stat_resistance_magic': 'damage_mod_magic',
                    'stat_resistance_physical': 'damage_mod_physical',
                    'stat_weakness_flame': 'damage_mod_flame', # identical to stat_resistance_flame as far as I know
                   
                    'stat_armour': 'armour',
                    'stat_missile_block_chance': 'missile_block_chance',
                   
                    'stat_melee_attack': 'melee_attack',
                    'stat_melee_defence': 'melee_defence',
                    }


# The stat effects can be found in the:
# special_abilty_phase_stat_effects_tables
name_and_effects = {}
with open("stat_effects_tables.tsv") as fd:
    rd = csv.reader(fd, delimiter="\t", quotechar='"')
    for n,row in enumerate(rd):
        if row[0] == " ":
            print(row)
        if n < 3:
            continue
        if row[0] not in name_and_effects:
            name_and_effects[row[0]] = [(float(row[1]),stat_translator[row[2]],row[3])]
        else:
            name_and_effects[row[0]].append((float(row[1]),stat_translator[row[2]],row[3]))

effects_dict = {}
for name,effects in name_and_effects.items():
    E = TWWEffect(name,effects)
    effects_dict[str(E)] = E


