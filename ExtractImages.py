# The UI file is extracted from the game using the File Pack Manager
# Its large so ts not included in this repository to hide the entire folder
# it contains a .gitignore that just says * and the same method is used to 
# prevent the FactionFlags folder from being uploaded as well

import os
import shutil

def extract_flags():
    cur_dir = os.getcwd()
    flags1 = cur_dir+"\\WarhammerUI\\flags"
    
    for r,d,f in os.walk(flags1):
        if f == []:
            continue
        faction_name = "_".join(r[len(flags1)+5:].split("_")[1:])
        for size in ["24","64","256"]:
            try:
                file24 = f"{r}\\mon_{size}.png"
                newfile24 = f"{cur_dir}\\FactionFlags\\{faction_name}_{size}.png"
                shutil.copyfile(file24,newfile24)
            except:
                print(f"{faction_name}_{size} not found")
    

                
extract_flags()