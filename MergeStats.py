## Here we are taking the raw data from the various tables and converting it
## into a useful form.

import numpy as np
import re
import linecache
import pandas as pd 
import pickle

## For convenience the linecache library allows us to quickly see a list of
## what traits there are and what their index is.
for i,l in enumerate(linecache.getline("Land_Units_Tables.csv",3).split("\t")):
    print(i,l)
    
for i,l in enumerate(linecache.getline("Melee_Weapons_Tables.csv",3).split("\t")):
    print(i,l)
    
for i,l in enumerate(linecache.getline("Main_Units_Tables.csv",3).split("\t")):
    print(i,l)

for i,l in enumerate(linecache.getline("Battle_Entities_Tables.csv",3).split("\t")):
    print(i,l)

for i,l in enumerate(linecache.getline("Mounts_Tables.csv",3).split("\t")):
    print(i,l)
    
for i,l in enumerate(linecache.getline("Battlefield_Engines_Tables.csv",3).split("\t")):
    print(i,l)

## Open the files to read them.
stat_file = open('Land_Units_Tables.csv', 'r')
weapon_file = open('Melee_Weapons_Tables.csv', 'r')
names_file = open('OnscreenNames.csv', 'r')
main_units_file = open('Main_Units_Tables.csv', 'r')
battle_entities_file = open('Battle_Entities_Tables.csv', 'r')
mounts_tables_file = open('Mounts_Tables.csv', 'r')
engines_tables_file = open('Battlefield_Engines_Tables.csv', 'r')

## To start with we will take the information from Melee_Weapons_Tables and place
## it into a dictionary. The name of each key will be the name of the weapon. This
## way as we work with each unit we can select the weapon it uses and the associated
## stats.
## Note that we skip the first three lines as they contain no data we want.
weapons = dict()
for i,line in enumerate(weapon_file):
    if i > 2:
        L = line.split("\t")
        weapons[L[3]] = [L[1],L[2],L[4],L[5],L[19]]
    
## Here we take in the data from the OnscreeNames file  
names = dict()
for i,line in enumerate(names_file):
    L = line.split("\t")
    if "_onscreen_" in L[0]:
        kn = re.sub("land_units_onscreen_name_","",L[0])
        names[kn] = L[1][1:-1]
        
## Here we take in the data from the Main_Units_Tables file
## For some insane reason there are a number of dummied out naval units on
## this list that share a land_unit keyname with actual units in the game. We
## filter them out.
main = dict()
for i,line in enumerate(main_units_file):
    if i > 2:
        L = line.split("\t")
        if "_shp_" not in L[17]:
            main[L[5]] = [L[2],L[6],L[19],L[8]]
            
entities = dict()
for i,line in enumerate(battle_entities_file):
    if i > 2:
        L = line.split("\t")
        entities[L[0]] = [L[3],L[6],L[13],L[21],L[23],L[17]]
        
mounts = dict()
for i,line in enumerate(mounts_tables_file):
    if i > 2:
        L = line.split("\t")
        mounts[L[0]] = L[2]
        
engines = dict()
for i,line in enumerate(engines_tables_file):
    if i > 2:
        L = line.split("\t")
        engines[L[4]] = L[7]

missile_weapons = pickle.load( open( "missileWeaponsDict.p", "rb" ) )


## Prepare a dictionary to hold the information we want about each unit.
traits = ['name','key_name','charge','armor','category','class','melee_A','melee_D',
          'BVL','BVI','damage','ap_damage','total_damage','ap_fraction',
          'attack_interval','faction','caste','models','weight_class','melee_weapon',
          'leadership','missile_weapon','MP_cost','missile_damage','missile_ap_damage',
          'missile_total_damage','missile_projectiles','missile_shots_per_volley',
          'ground_speed','mass','fly_speed','shield','HP','missile_ap_fraction',
          'missile_range','attributes','damage_mod_fire','damage_mod_magic',
          'damage_mod_physical','damage_mod_missiles','damage_mod_all']
units = dict()
for t in traits:
    units[t] = []

## Now we will gather up the information from the Land_Units_Tables so we can
## describe each unit.
## Note that we skip the first three lines as they contain no data we want.
for i,line in enumerate(stat_file):
    if i > 2:
        # The data is separated by tabs so that is how we split it
        L = line.split("\t")


        # Armor is a bit complicated. It is stored as string with a bunch of
        # information. The actual amount of armor is the last few characters.
        # A regular expression extracts what we want then we turn it into an
        # integer
        units['armor'].append(int(re.findall("\d+$",L[1])[0]))
        
        # These stats are simply integers and all we have to do is convert them
        # to that format.
        units['charge'].append(int(L[4]))
        units['melee_A'].append(int(L[12]))
        units['melee_D'].append(int(L[13]))
        units['leadership'].append(int(L[14]))
        units['damage_mod_fire'].append(int(L[49]))
        units['damage_mod_magic'].append(int(L[50]))
        units['damage_mod_physical'].append(int(L[52]))
        units['damage_mod_missiles'].append(int(L[53]))
        units['damage_mod_all'].append(int(L[54]))

        # These stats are best stored as strings so no change is needed.
        units['category'].append(L[3])
        units['class'].append(L[5])
        units['key_name'].append(L[9])
        units['melee_weapon'].append(L[20])
        units['missile_weapon'].append(L[21])
        
        #To get the shield we check if it exists then grab the fourth section
        if L[23] == "none":
            units['shield'].append(0)
        else:
            units['shield'].append(L[23].split("_")[3])
        
        # To get the faction we grab the third part of the keyname
        units['faction'].append(L[9].split("_")[2])
        
        units['attributes'].append(L[36])
        
        # Calculating HP is a bit wild!
        bonus = int(L[15])
        n_engines = int(L[51])
        n_mounts = int(L[19]) * max(1,n_engines)
        n_men = int(main[L[9]][1])
        # The unit, its mounts, and engines each have a certain amount of HP
        # which we get from the battle entities table.
        unitHP = int(entities[L[11]][5])
        engineHP = 0
        mountHP = 0
        if L[31] != '':
            engineHP = int(entities[engines[L[31]]][5])
        if L[16] != '':
            mountHP = int(entities[mounts[L[16]]][5])
        
        if n_engines > 0:
            engineHP += bonus
            if n_mounts > 0:
                engineHP += 1
            elif n_men > 0 and n_engines > 1:
                unitHP += bonus
        elif n_mounts > 1:
            mountHP += bonus
        else:
            unitHP += bonus
        
        units['HP'].append(int((n_men * unitHP + n_mounts * mountHP + n_engines * engineHP) * .75))
                
                
        
        ### Now we make use of the keyname to link to information in other
        ### dictionaries we created.
        
        
        # This really ugly line gets the friendly name
        units['name'].append(names['"'+L[9]+'"'])
        
        
        ## The main_units_tables hold a bunch of information
        additional = main[L[9]]
        units['caste'].append(additional[0])
        # Models are converted to the standard 75% large size
        units['models'].append(int(np.ceil(float(additional[1])*.75)))
        units['weight_class'].append(additional[2])
        units['MP_cost'].append(int(additional[3]))


        # Now we match the unit's weapon type to the information we put into
        # the weapons dictionary we prepared earlier and put that data into it.
        weap = weapons[L[20]]
        units['BVL'].append(int(weap[0]))
        units['BVI'].append(int(weap[1]))
        units['damage'].append(int(weap[2]))
        units['ap_damage'].append(int(weap[3]))
        units['total_damage'].append(int(weap[2])+int(weap[3]))
        units['ap_fraction'].append( int(weap[3]) / (int(weap[2])+int(weap[3])))
        
        # Attack interval is a not always a whole number so it needs to be
        # in floating point. It is also at the end of the line so we need
        # to remove the newline code.
        units['attack_interval'].append(float(re.sub("\n","",weap[4])))
        
        if L[21] != '':
            miss = missile_weapons[L[21]]
            units['missile_damage'].append(miss[13])
            units['missile_ap_damage'].append(miss[14])
            units['missile_total_damage'].append(miss[13]+miss[14])
            units['missile_projectiles'].append(miss[5])
            units['missile_shots_per_volley'].append(miss[47])
            units['missile_ap_fraction'].append(miss[14]/(miss[13]+miss[14]))
            units['missile_range'].append(miss[7])
            #units['reload_time'].append(miss[18]*1/((int(L[39])+100)/100))
        else:
            units['missile_damage'].append(0)
            units['missile_ap_damage'].append(0)
            units['missile_total_damage'].append(0)
            units['missile_projectiles'].append(0)
            units['missile_shots_per_volley'].append(0)
            units['missile_ap_fraction'].append(0)
            units['missile_range'].append(0)
            #units['reload_time'].append(0)
        
                
        if L[31] != '':
            eng = entities[engines[L[31]]]
            units['ground_speed'].append(float(eng[0])*10)
            units['mass'].append(int(eng[2]))
            units['fly_speed'].append(float(eng[3])*10)
        elif L[16] != '':
            mnt = entities[mounts[L[16]]]
            units['ground_speed'].append(float(mnt[0])*10)
            units['mass'].append(int(mnt[2]))
            units['fly_speed'].append(float(mnt[3])*10)
        else:
            man = entities[L[11]]
            units['ground_speed'].append(float(man[0])*10)
            units['mass'].append(int(man[2]))
            units['fly_speed'].append(float(man[3])*10)
            
            


unitsDF = pd.DataFrame(units)
pd.set_option('display.max_columns', 500)
#for i in ['caste','category','class','faction']:
#    print("{}: {}\n".format(i,unitsDF[i].unique()))

#print(unitsDF.columns.tolist())
pickle.dump(unitsDF, open( "unitsDF.p", "wb" ) )
pickle.dump(units, open( "unitsDict.p", "wb" ) )
unitsDF.to_csv("units.csv")

print(unitsDF.loc[unitsDF['key_name'].str.contains('princess')])

print(len(unitsDF.columns))