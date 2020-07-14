
def show_dict(D,superdict=""):
    for key,val in D.items():
        if type(val) == dict:
            print(f"##### begin {superdict}['{key}'] #####")
            show_dict(val,superdict=superdict+f"['{key}']")
            print(f"#####  end  {superdict}['{key}']  #####\n")
            
        elif type(val) == list:
            print(f"##### begin {superdict}['{key}'] #####")
            for n,i in enumerate(val):
                if type(i) == dict:
                    print(f"##### {superdict}['{key}'][{n}] #####\n")
                    show_dict(i,superdict=superdict+f"['{key}']")
                else:
                    print(f"##### {superdict}['{key}'][{n}] #####\n")
                    print(f"['{key}'][{n}]{val}\n")
            print(f"#####  end  {superdict}['{key}'] #####\n")
            
        else:
            print(f"{key}: {val}\n")

def show_unit_by_key(D,key):
    for unit in D:
        if key == unit["key"]:
            show_dict(unit)
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
    
    for j in J:
        if j['name'] == 'Azhag the Slaughterer on Skullmuncha':
            show_dict(j)
    
    # with open('TWWAbilities.json', encoding="utf8") as f:
    #     J = json.load(f)
    
    # for j in J:
    #     if j['name'] == 'Extra Powder':
    #         show_dict(j)
    #         print("############################")
    #         # break