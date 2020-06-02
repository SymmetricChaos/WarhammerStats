import pandas as pd
import linecache
import pickle

missile_junction_DF = pd.read_csv('Missile_Weapons_Tables.csv',sep='\t',header=2)
projectile_DF = pd.read_csv('Projectiles_Tables.csv',sep='\t',header=2)
land_units_DF = pd.read_csv('Land_Units_Tables.csv',sep='\t',header=2)


for i,l in enumerate(linecache.getline("Projectiles_Tables.csv",3).split("\t")):
    print(i,l)
    
missile_weapons = dict()
for i in land_units_DF['primary_missile_weapon'].values:
    if type(i) == str:
        proj = missile_junction_DF.loc[missile_junction_DF['key'] == i]['default_projectile']
        mstats = projectile_DF.loc[projectile_DF['key'] == proj.values[0]]
        missile_weapons[i] = mstats.values[0]
        
    
    
pickle.dump(missile_weapons, open( "missileWeaponsDict.p", "wb" ) )