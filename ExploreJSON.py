from UtilityFunctions import show_dict

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


if __name__ == '__main__':
    import json
    with open('unitsdata.json', encoding="utf8") as f:
        J = json.load(f)
    
    # for j in J:
    #     if 'Dragonback Slayers' in j['name']:
    #         show_dict(j,"")

    
    with open('TWWAbilities.json', encoding="utf8") as f:
        J = json.load(f)
    
    for j in J:
        if 'Dragonback' in j['name']:
            show_dict(j)
            break