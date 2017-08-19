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

# Encoding categorical data 
# Country Column
dataset$Country = factor(dataset$Country, 
                         levels = c('France', 'Spain', 'Germany'), # Creates a factor with three elements 
                         labels = c(1, 2, 3)) # Assign numbers to the categorical data 
# Purchased Column 
dataset$Purchased = factor(dataset$Purchased, 
                         levels = c('No', 'Yes'),
                         labels = c(0, 1)) 

# Splitting the dataset into the Training set and Test set
install.packages('caTools') # Install caTools
library(caTools) # Activate caTools 
set.seed(123) # Same as random set in python, could be any number 
split = sample.split(dataset$Purchased, SplitRatio = 0.8) # Prepare split method, 80% goes to training set  
# Splits data according to true or false output for each values from the above line
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

# Feature Scaling
training_set[, 2:3] = scale(training_set[, 2:3])
test_set[, 2:3] = scale(test_set[, 2:3])