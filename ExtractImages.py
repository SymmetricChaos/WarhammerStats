# The UI file is extracted from the game using the File Pack Manager
# Its large so ts not included in this repository to hide the entire folder
# it contains a .gitignore that just says * and the same method is used to 
# prevent the FactionFlags folder from being uploaded as well

import os
import shutil
cur_dir = os.getcwd()
flags = cur_dir+"\\ui\\flags"

faction_names = []

for r,d,f in os.walk(flags):
    if f == []:
        continue
#    # Horrible messy 
    faction_name = "_".join(r[len(flags)+5:].split("_")[1:])
    
    for size in ["24","64","256"]:
        try:
            file24 = f"{r}\\mon_{size}.png"
            newfile24 = f"{cur_dir}\\FactionFlags\\{faction_name}_{size}.png"
            shutil.copyfile(file24,newfile24)
        except:
            print(f"{faction_name}_{size} not found")