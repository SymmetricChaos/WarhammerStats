import pandas as pd


missile_junction_DF = pd.read_csv('Missile_Weapons_Tables.csv',sep='\t',header=2)
projectile_DF = pd.read_csv('Projectiles_Tables.csv',sep='\t',header=2)
land_units_DF = pd.read_csv('Land_Units_Tables.csv',sep='\t',header=2)


PMW = land_units_DF.loc[land_units_DF['key'].str.contains('_casket')]['primary_missile_weapon']

PROJ = missile_junction_DF.loc[missile_junction_DF['key'].str.contains(PMW.values[0])]

STAT = projectile_DF.loc[projectile_DF['key'] == PROJ.values[0][2]]

print(PMW)
print()
print(PROJ)
print()
print(STAT)


#print(land_units_DF['primary_missile_weapon'])
#print(missile_junction_DF['default_projectile'])
#print(projectile_DF['key'])