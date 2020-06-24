
def show_dict(D):
    for key,val in D.items():
        if type(val) == dict:
            print(f"\n####### begin {key} #######\n")
            show_dict(val)
            print(f"####### end {key} #######\n\n")
        else:
            print(f"{key}: {val}\n")

def show_dict_clean(D):
    for key,val in D.items():
        if type(val) == dict:
            print(f"\n####### begin {key} #######\n")
            show_dict(val)
            print(f"####### end {key} #######\n\n")
        else:
            if key in ["spells","abilities"]:
                print(f"{key}: {[line['name'] for line in val]}\n")
            elif key in ["attributes"]:
                print(f"{key}: {[line['key'] for line in val]}\n")
            else:
                print(f"{key}: {val}\n")

def show_unit_by_key(D,key):
    for unit in D:
        if key == unit["key"]:
            show_dict_clean(unit)
            break
            
def find_unit(D,name):
    
    name_list = []
    for unit in D:
        if name in unit["name"]:
            name_list.append((unit["name"],unit["key"]))
    
    if len(name_list) == 0:
        raise Exception(f"No units contain {name} in their name")
    
    if len(name_list) == 1:
        show_unit_by_key(D,name_list[0][1])
        
    else:               
        print("Multiple matches. Choose a unit")   
        for n,i in enumerate(name_list):
            print(n,i[0],i[1])
        x = int(input())
        show_unit_by_key(D,name_list[x][1])



def get_factions(D):
    fac = D["factions"]
    return [line["screen_name"] for line in fac]

def get_faction_group(D):
    return D["key"].split("_")[2]


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
        
if __name__ == '__main__':
    import json
    with open('unitsdata.json', encoding="utf8") as f:
        J = json.load(f)
        
        
    find_unit(J,"Ellyrian")