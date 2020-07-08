import csv
from UtilityFunctions import show_dict

class TWWEffect:
    
    def __init__(self,name,tooltip):
        self.name = name
        self.tooltip = tooltip
    
    # def __call__(self,unit):
        

# The stat effects can be found in the:
# special_abilty_phase_stat_effects_tables

effect_dict = {}

with open("stat_effects_tables.tsv") as fd:
    rd = csv.reader(fd, delimiter="\t", quotechar='"')
    for n,row in enumerate(rd):
        if n < 3:
            continue
        if row[0] not in effect_dict:
            effect_dict[row[0]] = [(float(row[1]),row[2],row[3])]
        else:
            effect_dict[row[0]].append((float(row[1]),row[2],row[3]))
            
show_dict(effect_dict)