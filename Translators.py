# Translate attributes from their internal name to their pretty name
attribute_pretty_name = {"berserk": "Berserk",
                         "cant_run": "Can't Run",
                         "causes_fear": "Fear",
                         "causes_terror": "Terror",
                         "charge_reflector": "Expert Charge Defence",
                         "charge_reflector_vs_large": "Charge Defence vs. Large",
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
                    
                    'scalar_speed': 'speed', # note multiple speeds
                    'scalar_charge_speed': 'charge_speed',# note multiple charge speeds, too
                    'stat_charge_bonus': 'charge_bonus', 
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

# Change a stat modifier from effect_bonus_value_ids_unit_sets_tables.tsv into a list we can use
tech_stat_translator = {
                        'armour_mod': ['armour','add'],
                        
                        'range_mod': ['range','mult'],
                        'ammo_mod': ['ammo','mult'],
                        'reload': ['reload_skill','add'],
                        
                        'charge_bonus': ['charge_bonus','mult'],
                        'charge_add': ['charge_bonus','add'],
                        
                        'melee_attack_mod': ['melee_attack','add'],
                        'melee_defence_mod': ['melee_defence','add'],
                        
                        'melee_damage_ap_mod_add': ['melee_ap_damage','add'],
                        'melee_damage_ap_mod_mult': ['melee_ap_damage','mult'],
                        'melee_damage_mod_add': ['melee_base_damage','add'],
                        'melee_damage_mod_mult': ['melee_base_damage','mult'],
                        
                        'missile_damage_ap_mod_add': ['ranged_ap_damage','add'],
                        'missile_damage_ap_mod_mult': ['ranged_ap_damage','mult'],
                        'missile_damage_mod_add': ['ranged_base_damage','add'],
                        'missile_damage_mod_mult': ['ranged_base_damage','mult'],
                        
                        'morale': ['leadership','add'],
                        
                        'unit_damage_resistance_flame_mod': ['damage_mod_flame','add'],
                        'unit_damage_resistance_all_mod': ['damage_mod_all','add'],
                        'unit_damage_resistance_missile_mod': ['damage_mod_missile','add'],
                        'unit_damage_resistance_physical_mod': ['damage_mod_physical','add'],
                        'unit_damage_resistance_magic_mod': ['damage_mod_magic','add'],
                        
                        'mod_land_movement_battle': ['speed','mult'],
                        
                        'damage_vs_infantry': ['melee_bonus_v_infantry','add'],
                        'damage_vs_large_entities': ['melee_bonus_v_large','add']
                        }

# Go from name code to the common name
faction_code_to_name = {'brt': "Brettonia",
                        'bst': "Beastmen",
                        'chs': "Warriors of Chaos",
                        'cst': "Vampire Coast",
                        'def': "Dark Elves",
                        'dwf': "Dwarfs",
                        'emp': "The Empire",
                        'grn': "Greenskins",
                        'hef': "High Elves",
                        'lzd': "Lizardmen",
                        'nor': "Norsca",
                        'skv': "Skaven",
                        'tmb': "Tomb Kings",
                        'vmp': "Vampire Counts",
                        'wef': "Wood Elves",
                        'teb': "Southern Realms",
                        'neu': "Neutral",
                        'huntmarshall': "The Empire"}