import json
import pandas as pd 
import pickle

with open('unitsdata.json', encoding="utf8") as f:
  J = json.load(f)
  
# Make a somewhat cleaner object to store
# We can expand later if we want
  
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

units = []

for unit in J:
    D = {"name": unit["name"],
         "health": unit["health"],
         "multiplayer_cost": unit["multiplayer_cost"],
         "mass": unit["mass"],
         "caste": unit["caste"],
         "category": unit["category"],
         "special_category": unit["special_category"],
         "entity_size": unit["entity_size"],
         "height": unit["height"],
         "radius": unit["radius"],
         "attributes": get_attributes(unit),
         "abilities": get_abilities(unit),
         "factions": get_factions(unit),
         "faction_group": get_faction_group(unit)
         
         }
    units.append(D)

unitsDF = pd.DataFrame(units)
pickle.dump(unitsDF, open( "unitsDF.p", "wb" ) )
pickle.dump(units, open( "unitsDict.p", "wb" ) )
unitsDF.to_csv("units.csv")