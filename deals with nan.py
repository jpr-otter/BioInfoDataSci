import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (12,9)


#creates the dataframe
data = pd.read_csv(r'C:\Users\Jenny\Desktop\GDBI files\NHANES.txt', delimiter = "\t")



#replace nan of a column with 0
data['Waist'] = data['Waist'].replace(np.nan, 0) 
data['BMI'] = data['BMI'].replace(np.nan, 0)
#data = data.replace(0, np.NaN)



# find the mean of non zero values from the columns
x_mean = (data['BMI'].loc[data['BMI'] != 0]).mean()
y_mean = (data['Waist'].loc[data['Waist'] != 0]).mean()
#means of x and y values / second mean to check if zeros in column ?
xx_mean = np.mean(x)
yy_mean = np.mean(y)



#summation  for forming r² and linReg equation
numerator = 0
denominator = 0
for i in range (len (x)):
    numerator += (x[i] - x_mean)*(y[i] - y_mean)
    denominator += (x[i] - x_mean)**2
    
m = numerator / denominator
b = y_mean - m * x_mean

y_linRegLine = m * x + b

print ("__________________________________")
#print ("numerator:", numerator )
#print ("denominator:", denominator)
print ("__________________________________")

print ("__________________________________")
print ("slope:", m )
print ("y-axis:", b)
print ("__________________________________")




#checks for nan

#x = float("nan")
#print(f"It's pd.isna  : {pd.isna(x)}")




#self explanatory
print ("__________________________________")
print ("mean x:", x_mean)
print ("check mean x but with zeros:", xx_mean)
print ("mean y:", y_mean)
print ("check mean y but with zeros:", yy_mean)
print ("__________________________________")
#print (x),(y)



#replaces all nan in column with 0
#data['Waist'] = data['Waist'].replace(np.nan, 0) 
#data['BMI'] = data['BMI'].replace(np.nan, 0)



#show all values of a column
#data['Waist'].tolist()
#data['BMI'].tolist()


#puts nan back into place for plotting THIS IS WEIRD sometimes if the line below is
# not a comment it will show a beautiful plot but only for the first time you run the code
# the second time you run the code the linRegLine vanishes
# and the linRegLine as a line not scattered seems to be way off
# so try running the code multiple times from switching the comment below on and off
data = data.replace(0, np.NaN)


#assigns data to axis
x = data.iloc[:, 10]#.values.reshape(-1, 1) 
y = data.iloc[:, 11]#.values.reshape(-1, 1) 



#plots the data with linReg
plt.scatter (x,y)
plt.plot ([min(x),max(x)], [min(y_linRegLine),max(y_linRegLine)], color = 'red')
plt.scatter (x,y_linRegLine, color = 'orange')
plt.show
