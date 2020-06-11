import numpy as np
import matplotlib.pyplot as plt
import pickle
import pandas as pd
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score, median_absolute_error
from UtilityFunctions import no_nonstandard, pretty_name

unitsDF = pickle.load( open( "unitsDF.p", "rb" ) )
unitsDF = no_nonstandard(unitsDF)

# Simple linear correlation take from a unitsDF dataframe
def simple_linear_model(X,Y):
    
    Xname = pretty_name(X.name)
    Yname = pretty_name(Y.name)
    
    X = X.values.reshape(-1,1)
    Y = Y.values.reshape(-1,1)
    
    model = linear_model.LinearRegression() 
    model.fit(X,Y)
    
    predicted_Y = model.predict(X)
    
    plt.scatter(X,Y)
    plt.xlabel(Xname)
    plt.ylabel(Yname)
    plt.plot(X,predicted_Y,
                color='red')
    
    R2 = r2_score(Y, predicted_Y)
    MAE = median_absolute_error(Y, predicted_Y)
    MSE = mean_squared_error(Y,predicted_Y)
    
    print(f"Simple Linear Model\n{Xname} vs {Yname}\n")
    print(f"R-squared: {round(R2,2)}")
    print(f"Mean Square Error: {round(MSE,2)}")
    print(f"Median Absolute Error: {round(MAE,2)}")
    plt.show()


def multiple_linear_model(Xs,Y):
    
    names = [pretty_name(n) for n in Xs.columns]
    print("Multiple Linear Model\n\nIndependent Variables:")
    for n in names:
        print(f"  {n}")
    
    print(f"\nDependent Variable:\n  {pretty_name(Y.name)}")
    
    Xs = Xs.values
    Y = Y.values.reshape(-1,1)
    
    model = linear_model.LinearRegression() 
    model.fit(Xs,Y)
    
    predicted_Y = model.predict(Xs)
    
    R2 = r2_score(Y, predicted_Y)
    MAE = median_absolute_error(Y, predicted_Y)
    MSE = mean_squared_error(Y,predicted_Y)
#    
#    print(f"Simple Linear Model\n{Xname} vs {Yname}\n")
    print(f"\nR-squared: {round(R2,2)}")
    print(f"Mean Square Error: {round(MSE,2)}")
    print(f"Median Absolute Error: {round(MAE,2)}")


if __name__ == '__main__':
    simple_linear_model(unitsDF["leadership"],
                        unitsDF["multiplayer_cost"])
    
    print()
    
    multiple_linear_model(unitsDF[["leadership","melee_attack","melee_defence",
                                   "melee_ap_ratio","health","armour","speed"]],
                        unitsDF["multiplayer_cost"])
    
    