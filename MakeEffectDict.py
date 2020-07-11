import csv
import re
import string

ability_key_to_name = {}
# Gotten from local_en.pack
with open("special_ability_phases.csv") as fd:
    rd = csv.reader(fd, delimiter="\t", quotechar='"')
    for row in rd:
        if row[1] != "":
            key = "_".join(row[0].split("_")[9:]) # split off unwanted part of key
            name = re.findall("[A-Z][A-Za-z \']*",row[1]) #grab just the name
            if name == "ph":
                continue
            ability_key_to_name[key] = name[0]

# Gotten from local_en.pack
with open("unit_abilities.csv", encoding='utf-8') as fd:
    rd = csv.reader(fd, delimiter="\t", quotechar='"')
    for row in rd:
        if "tooltip" not in row[0]:
            key = "_".join(row[0].split("_")[8:]) # split off unwanted part of key
            name = row[1]
            ability_key_to_name[key] = name
            
for k,v in ability_key_to_name.items():
    if "henri_le" in k:
        print(k)