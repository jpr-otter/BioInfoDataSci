import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
from scipy import stats
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

data_frame = pd.read_csv(r'C:\Users\Jenny\Desktop\GDBI files\NHANES.txt', delimiter = "\t")
data_frame['BMI'] = data_frame['BMI'].replace(np.nan)
data_frame['Waist'] = data_frame['Waist'].replace(np.nan)
x_BMI = data_frame.iloc[:,10].values.reshape(-1, 1) 
y_Waist = data_frame.iloc[:,11].values.reshape(-1, 1) 



linreg = LinearRegression (fit_intercept =True)
obj = linreg.fit (x_BMI, y_Waist)
trendline = linreg.predict (x_BMI)
plt.scatter (x_BMI,y_Waist, s = 2)
plt.plot (x_BMI, trendline, color = 'red')
plt.xlabel ('BMI')
plt.ylabel ('Waist')

plt.show

slope = linreg.coef_[0]
r_squared = r2_score (y_Waist,trendline)
print ()
print ("________________________________________________________________________________")
print ()
print ("The Coefficient of Determination (R²) of the dataset is:",r_squared)
print ("________________________________________________________________________________")
