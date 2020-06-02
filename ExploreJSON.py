import json

with open('unitsdata.json', encoding="utf8") as f:
  J = json.load(f)

def show_dict(D):
    for key,val in D.items():
        print(f"{key}: {val}\n")
        
def show_primary_melee_weapon(D):
    pmw = D["primary_melee_weapon"]
    show_dict(pmw)
        
def show_primary_missile_weapon(D):
    pmw = D["primary_missile_weapon"]
#    print(f"ammo: {pmw['ammo']}")
    show_dict(pmw["projectile"])

def show_secondary_missile_weapon(D):
    smw = D["secondary_missile_weapon"]
    print(f"ammo: {smw['ammo']}")
    show_dict(smw["projectile"])
        
def get_attributes(D):
    att = D["attributes"]
    return [line["key"] for line in att]

def get_abilities(D):
    att = D["abilities"]
    return [line["name"] for line in att]

def get_factions(D):
    fac = D["factions"]
    return [line["screen_name"] for line in fac]

def get_faction_group(D):
    return D["key"].split("_")[2]

def get_spells(D):
    spl = D["spells"]
    return [line["name"] for line in spl]
    

#unit = J[5]
#show_dict(unit)
#show_primary_melee_weapon(unit)
#show_primary_missile_weapon(unit)
#print(get_attributes(unit))
#print(get_abilities(unit))
#print(get_factions(unit))
#print(get_faction_group(unit))


#castes = set([])
#categories = set([])
#special_categories = set([])
#faction_groups = set([])
#
#for unit in J:
#    castes.add(unit["caste"])
#    categories.add(unit["category"])
#    special_categories.add(unit["special_category"])
#    faction_groups.add(get_faction_group(unit))
#
#print(castes)
#print(categories)
#print(special_categories)
#print(faction_groups)
        
        
for unit in J:
    if "Mortar" in unit["name"]:
        show_primary_missile_weapon(unit)
        break