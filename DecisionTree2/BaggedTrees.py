import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import BaggingClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split





unitsDF = pickle.load( open( "C:\\Users\\Alexander\\Documents\\Python Scripts\\WarhammerStuff\\unitsDF.p", "rb" ) )

LimitedDF = unitsDF.loc[(unitsDF['faction'] == 'brt') | 
        (unitsDF['faction'] == 'dwf') |
        (unitsDF['faction'] == 'hef') |
        (unitsDF['faction'] == 'def')]

LimitedDF = LimitedDF.loc[unitsDF['class'] != 'com']

factors = ['armor','charge','ground_speed','melee_A','melee_D',
           'mass','leadership','shield','missile_total_damage',
           'models','ap_fraction','total_damage','fly_speed',
           'missile_ap_fraction','missile_range','HP','damage_mod_magic',
           'damage_mod_physical','damage_mod_missiles']
X = LimitedDF[factors]
Y = LimitedDF['faction']


print(Y.value_counts(),"\n\n")

X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=.3)


baggedTrees = BaggingClassifier(n_estimators=50)
baggedTrees.fit(X_train, Y_train)

Y_pred = baggedTrees.predict(X_test)

acc_scr = accuracy_score(Y_test,Y_pred)

print("Bootstrap Aggregation Accuracy {:.3f}%".format(acc_scr*100))


ctr = 0
print()
for i in range(len(LimitedDF)):
    if ctr > 30:
        break
    #r = np.random.randint(0,len(LimitedDF))
    x = LimitedDF[factors].iloc[i].values.reshape(1,-1)
    pred_faction = baggedTrees.predict(x)
    true_faction = LimitedDF['faction'].iloc[i]
    
    if pred_faction[0] == true_faction:
        pass
    else:
        ctr += 1
        true_name = LimitedDF['name'].iloc[i]
        print(true_name,pred_faction[0],true_faction)
