import pickle
from pathlib import Path
effects_dict = pickle.load( open( str(Path(__file__).parent)+"\\DataFiles\\effectsDict.p", "rb" ) )
techs_dict = pickle.load( open( str(Path(__file__).parent)+"\\DataFiles\\techsDict.p", "rb" ) )

print(effects_dict["Heroic Killing Blow"].display())
print(techs_dict["Swiftsense"].display())
print(effects_dict["Tombstrike"].display())