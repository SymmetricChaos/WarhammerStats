import pickle
import random
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.metrics import accuracy_score
from AnalysisFunctions import decisionTreeStruct
import matplotlib.pyplot as plt

random.seed(1000)

unitsDF = pickle.load( open( "unitsDF.p", "rb" ) )

LimitedDF = unitsDF.loc[(unitsDF['faction'] == 'brt') | (unitsDF['faction'] == 'dwf')]


factors = ['armor','ground_speed','melee_A','melee_D']
X = LimitedDF[factors]
Y = LimitedDF['faction']


## A random forest classifier.
decisionTree = DecisionTreeClassifier(max_depth=2)
decisionTree.fit(X, Y)

Y_pred = decisionTree.predict(X)

acc_scr = accuracy_score(Y,Y_pred)
fea_imp = decisionTree.feature_importances_

print("Decision Tree Accuracy {:.3f}%".format(acc_scr*100))

export_graphviz(decisionTree,out_file='brt_vs_dwf_decision_tree_small.dot',
                class_names=['brt','dwf'],feature_names=factors,rounded=True)

#print("\nFeature Importance:")
#for i,j in zip(factors,fea_imp):
#    print("{:<20}: {:.3f}".format(i,j))

#decisionTreeStruct(decisionTree)
# https://dreampuf.github.io/GraphvizOnline/

#print(unitsDF.columns)

