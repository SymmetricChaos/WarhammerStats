# The UI file is extracted from the game using the File Pack Manager
# Its large so it is not included in this repository. To hide the entire folder
# it contains a .gitignore that just says * and the same method is used to 
# prevent the FactionFlags folder from being uploaded as well

import os
import shutil

def extract_flags():
    cur_dir = os.getcwd()
    flags = cur_dir+"\\WarhammerUI\\flags"
    
    for r,d,f in os.walk(flags):
        if f == []:
            continue
        faction_name = "_".join(r[len(flags)+5:].split("_")[1:])
        for size in ["24","64","256"]:
            try:
                oldfile = f"{r}\\mon_{size}.png"
                newfile = f"{cur_dir}\\FactionFlags\\{faction_name}_{size}.png"
                shutil.copyfile(oldfile,newfile)
            except:
                print(f"{faction_name}_{size} not found")
    
def extract_infopics():
    cur_dir = os.getcwd()
    units = cur_dir+"\\WarhammerUI\\units\\infopics"
    
    for r,d,f in os.walk(units):
        for i in f:
            oldfile = f"{r}\\{i}"
            newfile = f"{cur_dir}\\UnitPics\\{i}"
            shutil.copyfile(oldfile,newfile)
            
def extract_unit_icons():
    cur_dir = os.getcwd()
    units = cur_dir+"\\WarhammerUI\\units\\icons"
    
    for r,d,f in os.walk(units):
        for i in f:
            oldfile = f"{r}\\{i}"
            newfile = f"{cur_dir}\\UnitIcons\\{i}"
            shutil.copyfile(oldfile,newfile)
            
#def extract_character_icons():
#    cur_dir = os.getcwd()
#    flags = cur_dir+"\\WarhammerUI\\portraits\\units"
#    
#    for r,d,f in os.walk(flags):
#        if f == []:
#            continue
#        faction_name = "_".join(r[len(flags)+5:].split("_")[1:])
#        for size in ["24","64","256"]:
#            try:
#                oldfile = f"{r}\\mon_{size}.png"
#                newfile = f"{cur_dir}\\FactionFlags\\{faction_name}_{size}.png"
#                shutil.copyfile(oldfile,newfile)
#            except:
#                print(f"{faction_name}_{size} not found")
#    

if __name__ == '__main__':       
#    extract_flags()
#    extract_infopics()
    extract_unit_icons()