effects_dict = pickle.load( open( "effectsDict.p", "rb" ) )

for e in effects_dict:
    if e == "Weeping Blade":
        print(effects_dict[e].display())