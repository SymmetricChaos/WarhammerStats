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
    print(f"ammo: {pmw['ammo']}")
    show_dict(pmw["projectile"])

def show_secondary_missile_weapon(D):
    smw = D["secondary_missile_weapon"]
    print(f"ammo: {smw['ammo']}")
    show_dict(smw["projectile"])
        
def show_attributes(D):
    att = D["attributes"]
    for line in att:
        print(line["key"])
        print()


unit = J[5]
#show_dict(unit)
#show_primary_melee_weapon(unit)
#show_primary_missile_weapon(unit)
show_attributes(unit)