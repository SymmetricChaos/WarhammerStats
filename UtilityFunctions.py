import numpy as np
import pickle
import pandas as pd
pd.set_option('display.max_rows', 70)
pd.set_option('display.max_columns', 70)
unitsDF = pickle.load( open( "unitsDF.p", "rb" ) )

# Convert a trait name into a nicer looking version
def pretty_name(S):
    return " ".join(S.split("_")).title()





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
                'wef': "Wood Elves"}





### System for Removing Duplicate Characters That Share a Lore of Magic ###
# This should only be used in JSONtoDataframe if it is needed elsewhere the
# unitsDF_clean dataframe should just be loaded
lores = [" (Beasts)",
         " (Death)",
         " (Fire)",
         " (Heavens)",
         " (High)",
         " (Life)",
         " (Light)",
         " (Metal)",
         " (Shadows)",
         " (Dark)",
         " (Vampires)",
         " (Deep)",
         " (Plague)",
         " (Ruin)"]

def remove_lore(name):
    for lore in lores:
        if lore in name:
            name = name.replace(lore," ")
            while "  " in name:
                name = name.replace("  "," ")
            return name
    return name

def deduplicate_lore(units):

    names = units["name"]
    reduced_names = []
    for name in names:
        reduced_names.append(remove_lore(name))
    
    units_no_dupe_lores = units.replace(list(units["name"]),reduced_names)
    units_no_dupe_lores.drop_duplicates(subset="name",inplace=True)
    
    return units_no_dupe_lores





# I believe this is correct based on the description by the developers
# "Armour = Max damage reduction percentage. Min is always 50% of armour value.
#  To be more precise, any time base damage is dealt, the target rolls for 
#  armour. This armour roll is a random value between 50% and 100% of the 
#  armour stat. The armour roll is then applied as percentage damage 
#  reduction."
# Legacy calculation method by numerical simulation
#def average_armor_reduction_old(armor):
#    """Returns the proportion of base damage blocked by the given armor value"""
#    ar = np.linspace(armor/2,armor,1000)
#    ar = [min(x,100) for x in ar]
#    return np.mean(ar)/100

# Credit to u/Panthera__Tigris on reddit for coming up with this
def average_armor_reduction(armor):
    """Returns the proportion of base damage blocked by the given armor value"""
    if armor < 0:
        raise Exception("Armor cannot be less than 0")
    elif armor <= 100:
        return np.mean([armor,armor/2])/100
    elif armor <= 200:
        return (100*(armor-100)+(100-armor*0.5)*((armor*0.5+100)*0.5))/((armor-100)+(100-armor*0.5))/100
    else:
        raise Exception("Armor cannot be more than 200")

def average_damage_with_armor_raw(base_damage,ap_damage,armor):
    """
    Returns the average damage done by an attack with given base and ap damage
    against a target with given armor
    """
    armor_reduction = average_armor_reduction(armor)
    adjusted_base_damage = (1-armor_reduction)*base_damage
    return adjusted_base_damage+ap_damage

def average_damage_with_armor_ratio(total_damage,ap_ratio,armor):
    """
    Returns the average damage done by an attack with given total damage and 
    ap ratio against a target with given armor
    """
    ap_damage = total_damage*ap_ratio
    base_damage = total_damage-ap_damage
    return average_damage_with_armor_raw(base_damage,ap_damage,armor)





## Most functions below accept the argument "units" which should be a pandas
## DataFrame where each row is a unit description like the one created by
## JSONtoDataFrame

def random_unit(units):
    # randint returns a list, the comma just skips having to extract the only
    # element of the list
    r, = np.random.randint(0,1365,1)
    return units.iloc[r]

def unit_named(units,name):
    return units[units["name"]==name]

# Attributes, abilitiesm and spells are all stored as lists this extracts all
# the unique attributes, abilities, or spells in a given units dataframe
def all_attributes(units):
    attributes = set([])
    for unit_atts in units["attributes"]:
        for att in unit_atts:
            attributes.add(att)
    return sorted(attributes)
    
def all_abilities(units):
    abilities = set([])
    for unit_abs in units["abilities"]:
        for ab in unit_abs:
            abilities.add(ab)
    return sorted(abilities)

def all_spells(units):
    spells = set([])
    for unit_spells in units["spells"]:
        for spell in unit_spells:
            spells.add(spell)
    return sorted(spells)



# Version of a unitsDF that has no single entities
def no_single_entity(units):
    is_not_single_entity = units["unit_size"] != 1
    return units[is_not_single_entity]

# Version of a unitsDF that has no special units. Meaning these kinds are removed:
# 'blessed_spawning', 'crafted', 'elector_counts', 'mistwalker', 'renown', 'tech_lab'
def no_special_category(units):
    is_not_special_category = units["special_category"] == ""
    return units[is_not_special_category]

# Version of unitsDF without any summoned unitys
def no_summoned(units):
    # Tilde is the pandas NOT operator
    unbinding = ~units["key"].str.contains("summoned")
    return units[unbinding]

# Remove summon units, units with a special category like RoR, Mistwalker, etc
# Then also remove specific campaign only units
def no_nonstandard(units):
    units = no_summoned(units)
    units = no_special_category(units)
    
    nonstandard_keys = ["wh_dlc07_brt_cha_damsel_beasts_2",
                        "wh_dlc07_brt_cha_damsel_life_2",
                        "wh_main_brt_cha_damsel_2",
                        "wh_dlc05_brt_cha_armand_aquitaine_0",
                        "wh_dlc05_brt_cha_armand_aquitaine_1",  
                        "wh_dlc05_brt_cha_armand_aquitaine_2",
                        "wh_dlc05_brt_cha_armand_aquitaine_3",
                        "wh_dlc07_brt_cha_damsel_beasts_2",
                        "wh_dlc03_bst_cha_graktar_0",
                        "wh2_dlc14_def_cha_malus_darkblade_tzarkan_0_final_battle",
                        "wh2_dlc13_emp_cav_knights_blazing_sun_0_imperial_supply",
                        "wh_dlc05_grn_cha_snorko_one_finger_0",
                        "wh_dlc05_grn_cha_snorko_one_finger_1",
                        "wh_dlc05_grn_cha_snorko_one_finger_2",
                        "wh2_dlc15_grn_cha_night_goblin_warboss_0_big",
                        "wh2_dlc15_hef_mon_forest_dragon_0",
                        "wh2_main_lzd_cha_slann_mage_priest_campaign_0",
                        "wh2_main_lzd_inf_temple_guards_nakai",
                        "wh2_main_lzd_cav_horned_ones_0_nakai",
                        "wh2_dlc13_lzd_mon_sacred_kroxigors_0_nakai",
                        "wh2_main_lzd_mon_kroxigors_nakai",
                        "wh2_dlc12_lzd_cav_terradon_riders_0_tlaqua",
                        "wh2_dlc12_lzd_cav_terradon_riders_1_tlaqua",
                        "wh2_dlc12_lzd_mon_ancient_stegadon_1_nakai",
                        "wh2_dlc12_lzd_mon_bastiladon_3_nakai",
                        "wh_dlc01_nor_cha_chaos_sorcerer_lord_0",
                        "wh_dlc01_nor_cha_chaos_sorcerer_lord_1",
                        "wh_main_nor_cha_chaos_sorcerer_0",
                        "wh_main_nor_cha_chaos_sorcerer_1",
                        "wh_main_nor_mon_chaos_warhounds_1",
                        "wh2_dlc14_skv_cha_deathmaster_snikch_tzarkan_0",
                        "wh2_main_skv_inf_stormvermin_0_quest",
                        "wh_pro03_vmp_cha_krell_campaign_0",
                        "wh_pro03_vmp_cha_krell_campaign_1",
                        "wh_pro03_vmp_cha_krell_campaign_2",
                        "wh_pro03_vmp_cha_krell_campaign_3",
                        "wh_pro03_vmp_cha_krell_0",
                        "wh2_dlc11_vmp_inf_crossbowmen",
                        "wh2_dlc11_vmp_inf_handgunners"
                        ]
    
    for unwanted in nonstandard_keys:
        units = units[~units["key"].str.contains(unwanted)]
    
    return units

def all_with_ability(units,ability):
    has_ability = []
    for L in units["abilities"]:
        if ability in L:
            has_ability.append(True)
        else:
            has_ability.append(False)
    return units[has_ability]

def all_with_attribute(units,attribute):
    has_attribute = []
    for L in units["attributes"]:
        if attribute in L:
            has_attribute.append(True)
        else:
            has_attribute.append(False)
    return units[has_attribute]

def all_from_faction(units,faction_group):
    faction = units["faction_group"] == faction_group
    return units[faction]



if __name__ == '__main__':
    
    print(random_unit(unitsDF))
    
    print(all_abilities(unitsDF))
    print(all_attributes(unitsDF))
    
#    unitsDF_filtered = no_nonstandard(unitsDF)
    
    
#    print(100/average_damage_with_armor_ratio(100,.7,200))
#    print(no_single_entity(unitsDF))
    
#    print(all_with_ability(unitsDF,"Foe-Seeker"))
    
#    print(all_with_attribute(unitsDF,"strider"))
#    print(no_summoned(unitsDF))
#    print(unit_named(unitsDF,"Zombies"))
    
#    for ar in [9,10,11,12,13,75,150]:
#        print(average_armor_reduction(ar))
#        print(average_armor_reduction_old(ar))