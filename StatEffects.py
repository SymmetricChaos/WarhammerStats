import csv
from TWWObjects import TWWEffect

# Translate stats to names used in the unitsDF
stat_translator = {
                    'stat_reloading': 'reload_skill',
                    
                    'scalar_missile_explosion_damage_base': 'explosion_base_damage',
                    'scalar_missile_explosion_damage_ap': 'explosion_ap_damage',
                    
                    'stat_melee_damage_base': 'melee_base_damage', 
                    'stat_melee_damage_ap': 'melee_ap_damage',
                    'scalar_splash_attack_power': 'melee_splash_attack_multiplier',
                    
                    'scalar_missile_damage_ap': 'ranged_ap_damage',
                    'scalar_missile_damage_base': 'ranged_base_damage',
                    'scalar_missile_range': 'range',
                    'stat_accuracy': 'stat_accuracy',
                    
                    'scalar_speed': 'speed', # note multiple speed
                    'scalar_charge_speed': 'charge_speed',
                    'stat_charge_bonus': 'charge_bonus', # note multiple charge speeds, too
                    'scalar_entity_acceleration_modifier': 'acceleration',
                    'scalar_entity_deceleration_modifier':  'deceleration',
                    
                    'scalar_dealt_collision_knocked_down_threshold_modifier': 'UNUSED_scalar_dealt_collision_knocked_down_threshold_modifier',
                    'scalar_dealt_collision_knocked_flying_threshold_modifier': 'UNUSED_scalar_dealt_collision_knocked_flying_threshold_modifier',
                    'scalar_dealt_collision_knocked_back_threshold_modifier': 'UNUSED_scalar_dealt_collision_knocked_back_threshold_modifier',
                    'scalar_bracing': 'UNUSED_scalar_bracing',
                    'scalar_miscast_chance': 'UNUSED_scalar_miscast_chance', # currently unused, add this?
                    
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
# Need to find a way to get correct names
name_and_effects = {}
with open("stat_effects_tables.tsv") as fd:
    rd = csv.reader(fd, delimiter="\t", quotechar='"')
    for n,row in enumerate(rd):
        if n < 3:
            continue
        if row[0] not in name_and_effects:
            name_and_effects[row[0]] = [(float(row[1]),stat_translator[row[2]],row[3])]
        else:
            name_and_effects[row[0]].append((float(row[1]),stat_translator[row[2]],row[3]))
            
name_and_effects_raw = {}
with open("stat_effects_tables.tsv") as fd:
    rd = csv.reader(fd, delimiter="\t", quotechar='"')
    for n,row in enumerate(rd):
        if n < 3:
            continue
        if row[0] not in name_and_effects_raw:
            name_and_effects_raw[row[0]] = [(float(row[1]),row[2],row[3])]
        else:
            name_and_effects_raw[row[0]].append((float(row[1]),row[2],row[3]))

effects_dict = {}
for name,effects in name_and_effects.items():
    E = TWWEffect(name,effects)
    effects_dict[E.pretty_name] = E

if __name__ == '__main__':
    import json
    import pickle
    
    with open('stat_effects_raw.json', 'w') as fp:
        json.dump(name_and_effects_raw, fp)
    
    pickle.dump(effects_dict, open( "effectsDict.p", "wb" ) )