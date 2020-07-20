import pickle
import os
from Stats.TWWObjects import TWWUnit
from Stats.TWWEffect import TWWEffect
from Stats.UtilityFunctions import select_unit, average_armor_reduction, \
                             average_damage_with_armor_raw, \
                             average_damage_with_armor_ratio

data_dir = os.path.dirname(__file__)

unitsDF = pickle.load( open( data_dir+"\\WorkedFiles\\unitsDF.p", "rb" ) )
unitsDF_clean = pickle.load( open( data_dir+"\\WorkedFiles\\unitsDF_clean.p", "rb" ) )
unitsDF_dedupe = pickle.load( open( data_dir+"\\WorkedFiles\\unitsDF_dedupe.p", "rb" ) )
effect_dict = pickle.load( open( data_dir+"\\WorkedFiles\\effectsDict.p", "rb" ) )

__all__ = ["unitsDF","unitsDF_clean","unitsDF_dedupe","effect_dict",
           "TWWUnit",
           "select_unit",
           "average_armor_reduction","average_damage_with_armor_raw",
           "average_damage_with_armor_ratio",
           ]