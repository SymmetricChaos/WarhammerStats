# Translate attributes from their internal name to their pretty name
attribute_pretty_name = {"berserk": "Berserk",
                         "cant_run": "Can't Run",
                         "causes_fear": "Fear",
                         "causes_terror": "Terror",
                         "charge_reflector": "Charge Defense",
                         "charge_reflector_vs_large": "Charge Defence Against Large",
                         "construct": "Construct",
                         "encourages": "Encourage",
                         "expendable": "Expendable",
                         "fatigue_immune": "Perfect Vigor",
                         "guerrilla_deploy": "Vanguard Deployment",
                         "hide_forest": "Hide (Forest)",
                         "ignore_trees": "Woodsman",
                         "immune_to_psychology": "Immune to Psychology",
                         "mounted_fire_move": "Fire While Moving",
                         "rampage": "Rampage",
                         "snipe": "Snipe",
                         "stalk": "Stalk",
                         "strider": "Strider",
                         "unbreakable": "Unbreakable",
                         "undead": "Undead",
                         "unspottable": "Unspottable",
                         "wallbreaker": "Wallbreaker"}

# Translate the names of affected stats to the ones used in unitsDF
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