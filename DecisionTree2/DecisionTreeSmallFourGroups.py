import pickle
import random
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.metrics import accuracy_score


unitsDF = pickle.load( open( "C:\\Users\\Alexander\\Documents\\Python Scripts\\WarhammerStuff\\unitsDF.p", "rb" ) )

LimitedDF = unitsDF.loc[(unitsDF['faction'] == 'brt') | 
        (unitsDF['faction'] == 'dwf') |
        (unitsDF['faction'] == 'hef') |
        (unitsDF['faction'] == 'def')]

factors = ['armor','charge','ground_speed','melee_A','melee_D',
           'mass','leadership','shield','missile_total_damage',
           'models','ap_fraction','total_damage','fly_speed',
           'MP_cost','missile_ap_fraction']
X = LimitedDF[factors]
Y = LimitedDF['faction']


decisionTree = DecisionTreeClassifier(max_depth=4)
decisionTree.fit(X, Y)

Y_pred = decisionTree.predict(X)

acc_scr = accuracy_score(Y,Y_pred)
fea_imp = decisionTree.feature_importances_

print("Decision Tree Accuracy {:.3f}%".format(acc_scr*100))

export_graphviz(decisionTree,out_file='four_group_decision_tree_small.dot',
                class_names=['brt','dwf','hef','def'],feature_names=factors,rounded=True,
                filled=True)