# Stats for the Stat Throne

Data is mainly from twwstats.com and many thanks to ciment on Discord helping out.

## Useage

> IDK how to make a proper package with data sets in it, help!

You need Pandas installed.
Clone the repo. (You might have to add it to your PythonPath, too)
Then make a file inside your copy.

Load the units data frame using: `pickle.load( open( "DataFiles\\unitsDF.p", "rb" ) )`. Import the `select_unit` function from `UtiltiyFunctions` (you don't have to but it will save you a lot of bother) and from `TWWUnit` from TWWObjects.

Example of use
```
my_unit = TWWUnit(select_unit(unitsDF,"Phoenix Guard"))
my_unit.set_fatigue("exhausted")
my_unit.toggle_effect("Martial Mastery")
my_unit.set_rank(7)
print(my_unit.unit_card)

| Phoenix Guard (High Elves)
| Halberd Infantry
| Units: 75
| Rank: 7
|
| HP               6300
| Armour           75
| Leadership       97
| Speed            32
| Melee Attack     42
| Melee Defence    56
| Weapon Strength  34 (11\23) BvL:20
| Charge Bonus     7
|
| Physical Resist  30%
|
| Fatigue: Exhausted
|
| Attributes: Expert Charge Defence, Fear, Hide
|    (Forest)
| Abilities: Martial Mastery
|
| Active Effects: Martial Mastery
```