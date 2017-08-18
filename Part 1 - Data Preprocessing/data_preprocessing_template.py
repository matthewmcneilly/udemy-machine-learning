# Data Preprocessing Template

# Importing the libraries
import numpy as np # for mathematical tools
import matplotlib.pyplot as plt # for plotting tools 
import pandas as pd # for importing and managing data sets 

# Importing the dataset
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].values # Take all the lines (:) and the columns (, :) except the last one (-1)  
y = dataset.iloc[:, 3].values # Take all the lines and the last column 

# Take care of missing data 
from sklearn.preprocessing import Imputer 
# Fill the missing values (NaN) with the mean average of the columns 
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
imputer = imputer.fit(X[:, 1:3]) # Grab the second and third column 
X[:, 1:3] = imputer.transform(X[:, 1:3]) # Replace missing value with average 

# Encoding categorical data 
from sklearn.preprocessing import LabelEncoder, OneHotEncoder 
labelencoder_X = LabelEncoder()
""" 
Encodes first column as numbers (France === 0)
so that they can be used in mathematical equations
"""
X[:, 0] = labelencoder_X.fit_transform(X[:, 0]) 
"""
Encode dummy variables
ensuring equations dont attribute an order to the categorical variables 
eg. France cant be greater than Germany, doesnt make any sense.  
So it creates a column to represent each categorical variable using 1's and 0's
as true or false
"""  
onehotencoder = OneHotEncoder(categorical_features = [0])
X = onehotencoder.fit_transform(X).toarray()
# Encode the last column 
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y) 




# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)"""