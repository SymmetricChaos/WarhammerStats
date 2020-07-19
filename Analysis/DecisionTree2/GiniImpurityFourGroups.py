import pickle
import random
import matplotlib.pyplot as plt
from itertools import product
import numpy as np


def gini_impurity(L):
    N = np.sum(L)
    out = 0
    for i in L:
        out += (i/N)*(i/N)
    return 1-out

unitsDF = pickle.load( open( "C:\\Users\\Alexander\\Documents\\Python Scripts\\WarhammerStuff\\unitsDF.p", "rb" ) )

LimitedDF = unitsDF.loc[(unitsDF['faction'] == 'brt') | 
        (unitsDF['faction'] == 'dwf') |
        (unitsDF['faction'] == 'hef') |
        (unitsDF['faction'] == 'def')]

N = LimitedDF.shape[0]

for brk in range(30,31):
    
    a = np.linspace(0,1,20)
    b = np.linspace(.9,0,20)
    Lgrd = product(a+.3,b)
    
    Rgrd = product(a+1.4,b)
    
    Lctr = [0,0,0,0]
    Rctr = [0,0,0,0]
    X = []
    Y = []
    C = []
    facpos = LimitedDF.columns.get_loc('faction')
    tarpos = LimitedDF.columns.get_loc('ground_speed')
    for i in LimitedDF.values:
        faction = i[facpos]
        grspeed = i[tarpos]
        
        if grspeed <= brk:
            if faction == 'brt':
                Lctr[0] += 1
            if faction == 'dwf':
                Lctr[1] += 1
            if faction == 'hef':
                Lctr[2] += 1
            if faction == 'def':
                Lctr[3] += 1

        if grspeed > brk:
            if faction == 'brt':
                Rctr[0] += 1
            if faction == 'dwf':
                Rctr[1] += 1
            if faction == 'hef':
                Rctr[2] += 1
            if faction == 'def':
                Rctr[3] += 1
        
        
        if grspeed > brk:
            z = next(Lgrd)
            X.append(z[0])
            Y.append(z[1])
        else:
            z = next(Rgrd)
            X.append(z[0])
            Y.append(z[1])
        
        if faction == 'brt':
            C.append('gold')
            
        if faction == 'dwf':
            C.append('blue')
            
        if faction == 'def':
            C.append('purple')
    
        if faction == 'hef':
            C.append('lightblue')
            
            
    impurityL = gini_impurity(Lctr)
    impurityR = gini_impurity(Rctr)
    
    plt.gcf().set_size_inches(20,10)        
    plt.scatter(X,Y,color=C,s=500,alpha=.75,edgecolor='black',linewidth=3)
    plt.axis('off')
    plt.title('Gini Impurity for Speed of {}'.format(brk),
              size=22)
    plt.ylim(-.1,1.2)
    plt.xlim(-.1,2.2)
    plt.axvline(1.3,color='k')
    plt.text(.3,1,"Above = {:.3f}".format(impurityL),size=20)
    plt.text(1.4,1,"Below = {:.3f}".format(impurityR),size=20)
    plt.savefig("Gini_Impurity{}.png".format(brk))
    plt.show()