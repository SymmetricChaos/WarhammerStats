import pickle
import os
from TWWObjects import TWWUnit
from UtilityFunctions import select_unit, average_armor_reduction, \
                             average_damage_with_armor_raw, \
                             average_damage_with_armor_ratio

cur_dir = os.getcwd()

unitsDF = pickle.load( open( cur_dir+"\\WorkedFiles\\unitsDF.p", "rb" ) )
unitsDF_clean = pickle.load( open( cur_dir+"\\WorkedFiles\\unitsDF_clean.p", "rb" ) )
unitsDF_dedupe = pickle.load( open( cur_dir+"\\WorkedFiles\\unitsDF_dedupe.p", "rb" ) )

__all__ = ["unitsDF","unitsDF_clean","unitsDF_dedupe",
           "TWWUnit",
           "select_unit",
           "average_armor_reduction","average_damage_with_armor_raw",
           "average_damage_with_armor_ratio"]