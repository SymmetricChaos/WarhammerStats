import numpy as np
import matplotlib.pyplot as plt
import pickle
import pandas as pd
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score

unitsDF = pickle.load( open( "unitsDF.p", "rb" ) )

melee_attack = unitsDF["melee_attack"].values.reshape(-1,1)
melee_defence = unitsDF["melee_defence"].values.reshape(-1,1)


model = linear_model.LinearRegression() 
model.fit(melee_attack,melee_defence)

predicted_melee_defence = model.predict(melee_attack)

plt.scatter(melee_attack,melee_defence)
plt.xlabel("Melee Attack")
plt.ylabel("Melee Defence")
plt.plot(melee_attack,predicted_melee_defence,
            color='red')