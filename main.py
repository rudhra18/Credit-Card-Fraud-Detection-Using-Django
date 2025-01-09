import pandas as pd
import numpy as np
from sklearn . preprocessing import StandardScaler
from sklearn . model selection import train
test split
from sklearn . linear model import LogisticRegression
from sklearn . metrics import confusion matrix , accuracy score
 
#Load the credit card data
data = pd. read csv(”creditcard . csv”)

# Normalize the ”Amount” column
scaler = StandardScaler ()
data [ ’normAmount’] = scaler . fit transform ( data [ ’Amount’ ]. values . reshape (−1, 1) )
data = data . drop ([ ’Time’ , ’Amount’] , axis=1)

# Split the data into training and testing sets
 
t rain , X test , y train , y
t e st = train
t e s t size =0.25 , random state=42)

19 model = LogisticRegression ()
20 model . fit ( X train , y,train )
pred = model. predict ( X test )
# Evaluate the model’s performance
conf mat = confusion matrix ( y
test , y
test split ( data . drop ( ’Class ’ , axis =1) , data [ ’Class ’] ,pred )
print (” Confusion Matrix :\n” , conf mat )
print (” Accuracy Score :\n” , accuracy score ( ytest , y, pred ) )

# Calculate the number of non−fraudulent and fraudulent transactions
num non fraud = conf mat [0][0] + conf mat [0][1]
num fraud = conf mat [1][0] + conf mat [1][1]
print (”Number of non−fraudulent transactions :” , num non fraud)
print (”Number of fraudulent transactions :” , num fraud)
