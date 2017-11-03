# Simple Linear Progression (y = b0 + b1 * x)

"""
Dependent Variable (y) - Data which depends on something else (eg. Salary, Grade)
Independent Variable (x) - Impacts the dependent variable 
Coeffiecient (b1) - Proportion of the impact of the independent to dependent variable (i.e. slope of the line)  
Constant (b0) - The starting point where the line crosses the vertical axis (e.g. starting wage)
yi  -  Actual model data value(e.g. what he/she is earning)
yi^ - Model predicted value (e.g what he/she should be earning)

Find line of best fit: SUM (y - y^)-> min
"""



# Importing the libraries
import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd


# Importing the dataset
dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:, :-1].values #Independent Variable - Matrix of features
y = dataset.iloc[:, 1].values #Dependent Variable - Vector 


# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)


# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train) 
X_test = sc_X.transform(X_test)
sc_y = StandardScaler() 
y_train = sc_y.fit_transform(y_train)"""