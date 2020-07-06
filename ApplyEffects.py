import math

## Abilities that mutate a Pandas Series to apply the effect of an ability

# Abilities that effect the unit itself
def apply_stand_your_ground(unit):
    unit["melee_defence"] += 5
    
def apply_evasion(unit):
    unit["melee_defence"] += 5
    
def apply_bathed_in_blood(unit):
    unit["melee_attack"] += 5
    
def apply_freny(unit):
    unit["melee_attack"] += 8
    unit["melee_base_damage"] = math.ceil(unit["melee_base_damage"]*1.15)
    unit["melee_total_damage"] = unit["melee_base_damage"]+unit["melee_ap_damage"]
    
def apply_aura_of_protection(unit):
    unit['damage_mod_all'] += 12
    
def apply_primal_fury(unit):
    unit['melee_attack'] += 5
    
def apply_the_dark_mail(unit):
    unit['armour'] += 30
    unit['damage_mod_magic'] += 25
    
def apply_regeneration(unit):
    unit['damage_mod_flame'] -= 25
    
def apply_slaughterers_call(unit):
    unit['melee_attack'] += 9
    
def apply_braid_of_bordelaux(unit):
    unit['melee_bonus_v_large'] += 8
    
def apply_fleur_de_lys_banner(unit):
    unit['melee_attack'] += 9
    unit['melee_defence'] += 9
    
def apply_aura_of_the_lady(unit):
    unit['damage_mod_magic'] += 12
    
def apply_blessing_of_the_lady(unit):
    unit['damage_mod_physical'] += 20



# Abilities that affect enemies
def apply_crush_the_weak(unit):
    unit["melee_attack"] -= 5
    unit["melee_defence"] -= 5
    
def apply_the_white_cloak_of_ulric(unit):
    unit["melee_attack"] -= 9
    
def apply_blinding_radiance(unit):
    unit["melee_attack"] -= 9
    
def apply_mist_of_the_lady(unit):
    unit['melee_attack'] -= 5
