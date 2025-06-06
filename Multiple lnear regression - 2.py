# -*- coding: utf-8 -*-
"""Copy of multiple_linear_regression.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18-SSij3AcnYHJxGW2oqmeBEzhmecy-sJ
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv("Housing prices.csv")
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

from sklearn.impute import SimpleImputer

imputer = SimpleImputer(missing_values= np.nan, strategy= "most_frequent")
im = SimpleImputer(missing_values=np.nan, strategy= "mean")
imputer.fit(X[:, 3:4])
X[:, 3:4] = imputer.transform(X[:, 3:4])

imputer.fit(X[:, 5:6])
X[:, 5:6] = imputer.transform(X[:, 5:6])

im.fit(X[:, 1:2])
X[:, 1:2] = im.transform(X[:, 1:2])

im.fit(X[:, 2:3])
X[:, 2:3] = im.transform(X[:, 2:3])

im.fit(X[:, 4:5])
X[:, 4:5] = im.transform(X[:, 4:5])

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

ct = ColumnTransformer(transformers=[("encoder", OneHotEncoder(), [3,5])], remainder="passthrough")
X = np.array(ct.fit_transform(X))

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state = 1)

from sklearn.linear_model import LinearRegression

regressor = LinearRegression()
regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)
np.set_printoptions(precision=2)
print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1))