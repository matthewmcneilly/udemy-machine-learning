# Data Preprocessing Template

# Importing the dataset
dataset = read.csv('Data.csv')

# Take care of missing values 
# Age Columns
dataset$Age = ifelse(is.na(dataset$Age), # If no value 
  ave(dataset$Age, FUN = function(x) mean(x, na.rm = TRUE)), # Use the mean average  
  dataset$Age) # If there is a value use it 
# Salary Column 
dataset$Salary = ifelse(is.na(dataset$Salary),
  ave(dataset$Salary, FUN = function(x) mean(x, na.rm = TRUE)), 
  dataset$Salary) 

# Splitting the dataset into the Training set and Test set
# install.packages('caTools')
library(caTools)
set.seed(123)
split = sample.split(dataset$DependentVariable, SplitRatio = 0.8)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

# Feature Scaling
# training_set = scale(training_set)
# test_set = scale(test_set)