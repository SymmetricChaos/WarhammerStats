import pickle
from pathlib import Path
effects_dict = pickle.load( open( str(Path(__file__).parent)+"\\DataFiles\\effectsDict.p", "rb" ) )
techs_dict = pickle.load( open( str(Path(__file__).parent)+"\\DataFiles\\techsDict.p", "rb" ) )

print(f"Num Effects: {len(effects_dict)}")
print(f"Num Techs:   {len(techs_dict)}\n")

print("Some Effects\n")
print(effects_dict["Regeneration"].effect_card)
print(effects_dict["Heroic Killing Blow"].effect_card)
print(effects_dict["Frostbite!"].effect_card)
print(effects_dict["Tombstrike"].effect_card)

print("\n\nSome Technologies\n")
print(techs_dict["Swiftsense"].effect_card)


# print("\n\nEmpty Effects\n")
# for k,v in effects_dict.items():
#     if v.stat_effects == [] and v.other_effects == []:
#         print(v.effect_card)


# print("\n\nEmpty Technologies\n")
# for k,v in techs_dict.items():
#     if v.stat_effects == [] and v.other_effects == []:
#         print(v.effect_card)
