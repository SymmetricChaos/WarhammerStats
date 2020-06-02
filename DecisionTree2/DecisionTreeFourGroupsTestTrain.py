import pandas as pd
import numpy as np
import pickle
from sklearn.tree import DecisionTreeClassifier
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
           'MP_cost','missile_ap_fraction','damage_mod_magic']
X = LimitedDF[factors]
Y = LimitedDF['faction']


print(Y.value_counts(),"\n\n")

X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=.5)


decisionTree = DecisionTreeClassifier(max_depth=4,min_samples_leaf=5)
decisionTree.fit(X_train, Y_train)

Y_pred = decisionTree.predict(X_test)

acc_scr = accuracy_score(Y_test,Y_pred)
fea_imp = decisionTree.feature_importances_

print("Decision Tree Accuracy {:.3f}%".format(acc_scr*100))

#print("\nFeature Importance:")
#for i,j in zip(factors,fea_imp):
#    print("{:<20}: {:.3f}".format(i,j))


#export_graphviz(decisionTree,out_file='four_group_decision_tree_large_test_train.dot',
#                class_names=['brt','dwf','hef','def'],feature_names=factors,rounded=True,
#                filled=True)


ctr = 0
print()
for i in range(len(LimitedDF)):
    if ctr > 30:
        break
    #r = np.random.randint(0,len(LimitedDF))
    x = LimitedDF[factors].iloc[i].values.reshape(1,-1)
    pred_faction = decisionTree.predict(x)
    true_faction = LimitedDF['faction'].iloc[i]
    
    if pred_faction[0] == true_faction:
        pass
    else:
        ctr += 1
        true_name = LimitedDF['name'].iloc[i]
        print(true_name,pred_faction[0],true_faction)
