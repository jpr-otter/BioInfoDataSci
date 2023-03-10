import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

data = pd.read_csv(r'C:\Users\Jenny\Desktop\GDBI files\NHANES.txt', delimiter = "\t")
print (data)
print (data.head())
print ()

print ("-----------------")
print ("MINIMAL VALUES")
print ("-----------------")
print ()
min = (data.min())
print (min.to_string())
print ()

print ("-----------------")
print ("MAXIMUM VALUES")
print ("-----------------")
print ()
max = (data.max())
print (max.to_string())
print ()

print ("-----------------")
print ("MEAN VALUES")
print ("-----------------")
print ()
mean = (data.mean())
print (mean.to_string())
print ()

print ("-----------------")
print ("MEDIAN VALUES")
print ("-----------------")
print ()
median = (data.median())
print (median.to_string())
print ()
print ()

print ("-----------------")
print ("QUALITATIVE FEATURES")
print ("-----------------")
print ()

print ("-----------------")
print ("SEX")
print ("-----------------")
print ()
sex = (data ['Sex'].value_counts())
print (sex.to_string())
print ()
print ()

print ("-----------------")
print ("ETHNICITY")
print ("-----------------")
print ()
race = (data ['Race'].value_counts())
print (race.to_string())
print ()
print ()

print ("-----------------")
print ("LEVEL OF EDUCATION")
print ("-----------------")
print ()
edu = (data ['Education'].value_counts())
print (edu.to_string())
print ()
print ()

print ("-----------------")
print ("MARITAL STATUS")
print ("-----------------")
print ()
marry = (data ['Marital'].value_counts())
print (marry.to_string())
print ()
print ()

print ("-----------------")
print ("SEXUAL ORIENTATION")
print ("-----------------")
print ()
sexor = (data ['SexOrient'].value_counts())
print (sexor.to_string())
print ()
print ()
axx=data.hist (column = 'Sodium', bins = 50, sharex=True, sharey=True)
for ax in axx.flatten():
    ax.set_xlabel("Blood Sodium Levels")
    ax.set_ylabel("Individuals")

#plot = data.plot(x='Sodium',y='' ,kind="hist")
#plot.set_xlabel("X")
#plot.set_ylabel("Y")

weight = data.hist (column = 'Weight', bins = 200, sharex=True, sharey=True)
for ax in weight.flatten():
    ax.set_xlabel("Weight")
    ax.set_ylabel("Individuals")
    
age = data.hist (column = 'Age', bins = 100, sharex=True, sharey=True)
for ax in age.flatten():
    ax.set_xlabel("Age")
    ax.set_ylabel("Individuals")
    
income = data.hist (column = 'F_Income', bins = 200, sharex=True, sharey=True)
for ax in income.flatten():
    ax.set_xlabel("F_Income")
    ax.set_ylabel("Individuals")

#axarr = frame.hist(column='Age', by = 'Survived', sharex=True, sharey=True, layout = (2,2)

#for ax in axarr.flatten():
#    ax.set_xlabel("Age")
#    ax.set_ylabel("Individuals")




data.plot (kind = 'hist',
                  alpha = 0.7, 
                  bins = 100, 
                  title = 'Histogram of the whole Dataset', 
                  rot = 45, 
                  grid= True, 
                  figsize = (12,8),
                  fontsize = 15)
plt.xlabel ('Value')
plt.ylabel ('Individuals')


#x = data.iloc[:, 0].values.reshape(-1, 1)  # values converts it into a numpy array
#y = data.iloc[:, 1].values.reshape(-1, 1)  # -1 means that calculate the dimension of rows, but have 1 column
#linear_regressor = LinearRegression()  # create object for the class
#linear_regressor.fit(x, y)  # perform linear regression
#y_pred = linear_regressor.predict(x)  # make predictions


#plt.scatter(x, y)
#plt.plot(x, y_pred, color='red')
#plt.show()

data.plot.scatter (x = "BMI",
                   y = "Waist",
                   s = 10,
                   figsize = (15,10),
                   title = "Correlation of waist circumference and BMI \n units unknown");





#print (data2 [(data2 ["Diet"]==4)])

#print (data.boxplot (column = ['weight','Time'], by ="Diet"))
#print ("-----------------")
#print (data2.boxplot (column = ['weight'], by ="Time"))
#print (data2.boxplot (column = ['weight'], by ="Chick"))
#print (data2[data2["Time"]>= 35].boxplot (column = ['weight'], by ="Diet", notch = True))
#print (data2.plot.scatter("Time","weight")) 
