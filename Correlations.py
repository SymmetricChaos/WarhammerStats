import numpy as np
import matplotlib.pyplot as plt
import pickle
import pandas as pd
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score, median_absolute_error

unitsDF = pickle.load( open( "unitsDF.p", "rb" ) )



# Simple linear correlation take from a unitsDF dataframe
def show_correlation(X,Y):
    Xname = " ".join(X.name.split("_"))
    Yname = " ".join(X.name.split("_"))
    X = X.values.reshape(-1,1)
    Y = Y.values.reshape(-1,1)
    
    
    model = linear_model.LinearRegression() 
    model.fit(X,Y)
    
    predicted_Y = model.predict(X)
    
    plt.scatter(X,Y)
    plt.xlabel(Xname.title())
    plt.ylabel(Yname.title())
    plt.plot(X,predicted_Y,
                color='red')
    
    R2 = r2_score(X, predicted_Y)
    MAD = median_absolute_error(X, predicted_Y)
    print(f"R-squared: {round(R2,2)}")
    print(f"Median Absolute Error: {round(MAD,2)}")


show_correlation(unitsDF["melee_attack"],unitsDF["melee_defence"])