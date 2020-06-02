import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split



unitsDF = pickle.load( open( "unitsDF.p", "rb" ) )

#Remove TEB and KSL from the data set since they are copies of EMP
LimitedDF = unitsDF.loc[(unitsDF['faction'] != 'teb') & (unitsDF['faction'] != 'ksl')]
#Remove lords and heroes
#LimitedDF = LimitedDF.loc[unitsDF['class'] != 'com']

factors = ['armor','charge','ground_speed','melee_A','melee_D',
           'mass','leadership','shield','missile_total_damage',
           'models','ap_fraction','total_damage','fly_speed',
           'missile_ap_fraction','missile_range','HP','damage_mod_magic',
           'damage_mod_physical','damage_mod_missiles']
X = LimitedDF[factors]
Y = LimitedDF['category']


print(Y.value_counts())
print('total units:',len(LimitedDF))

X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=.2)


## A random forest classifier.
randforest = RandomForestClassifier(criterion = "gini",
                               max_depth=None,
                               n_estimators=200)
randforest.fit(X_train, Y_train)

Y_pred = randforest.predict(X_test)

acc_scr = accuracy_score(Y_test,Y_pred)
fea_imp = randforest.feature_importances_

print("Decision Forest Accuracy {:.3f}%".format(acc_scr*100))

print("\nFeature Importance:")
for i,j in zip(factors,fea_imp):
    print("{:<20}: {:.3f}".format(i,j*100))


ctr = 0
print()
for i in range(len(LimitedDF)):
    if ctr > 40:
        break
    #r = np.random.randint(0,len(LimitedDF))
    x = LimitedDF[factors].iloc[i].values.reshape(1,-1)
    pred_faction = randforest.predict(x)
    true_faction = LimitedDF['category'].iloc[i]
    
    if pred_faction[0] == true_faction:
        pass
    else:
        ctr += 1
        true_name = LimitedDF['name'].iloc[i]
        print(true_name,pred_faction[0],true_faction)

