import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
from scipy import stats
#did i use those ML stuff ? probably not...
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


# create the dataframe

data_frame = pd.read_csv(r'C:\Users\Jenny\Desktop\GDBI files\NHANES.txt', delimiter = "\t")
#The National Health and Nutrition Examination Survey is a survey research program 
#conducted by the National Center for Health Statistics to assess the health and nutritional status 
#of adults and children in the United States, and to track changes over time.


# counts nans in data frame single column

count_BMI_nans = data_frame['BMI'].isnull().sum()
count_Waist_nans = data_frame['Waist'].isnull().sum()
count_Height_nans = data_frame['Height'].isnull().sum()

data_frame['Waist'].isnull().sum()

print ("__________________________________")
print ()
print ("How many values in column BMI are NaNs:", count_BMI_nans)
print ("How many values in column Waist are NaNs:", count_Waist_nans)
print ("How many values in column Height are NaNs:", count_Height_nans)

print ()
print ("__________________________________")


# drops all NaNs in the given columns

data_frame['BMI'] = data_frame['BMI'].replace(np.nan)
data_frame['Waist'] = data_frame['Waist'].replace(np.nan)


# counts AGAIN nans in data frame single column

count_BMI_nans = data_frame['BMI'].isnull().sum()
count_Waist_nans = data_frame['Waist'].isnull().sum()

if count_BMI_nans == 0:
    print ("No NaNs in column BMI")
elif count_BMI_nans > 0:
    print ("Still NaNs in column BMI left!!")

if count_Waist_nans == 0:
    print ("No NaNs in column Waist")
elif count_Waist_nans > 0:
    print ("Still NaNs in column Waist left!!")
if count_Height_nans == 0:
    print ("No NaNs in the column Height")
else: print ("Still NaNs in the column Height left!!") 

print ("__________________________________")
print ()
print ("How many values in column BMI are NaNs:", count_BMI_nans)
print ("How many values in column Waist are NaNs:", count_Waist_nans)
print ()
print ("__________________________________")


# TEST FOR NaNs


# prints all values of given columns

print ("__________________________________")
print ()
print ("The columns were cleaned, no NaNs anymore")
print ("Check the values of each columns for NaNs yourself")
print ()
print ("__________________________________")
print ()
#print ("BMI:\n\n", data_frame['BMI'].tolist())
print ()
print ("________________________________________________")
print ()
#print ("Waist:\n\n", data_frame['Waist'].tolist())
print ("Glucose:\n\n", data_frame['Glucose_mol'].tolist())

#can be deleted
#max_value_Glucose = ['Glucose_mol]'.max()
#print (max_value_Glucose)
                     
max_Glucose_value = data_frame['Glucose_mol'].max()
min_Glucose_value = data_frame['Glucose_mol'].min()
print ("Max Glucose:", max_Glucose_value)
print ("Min Glucose:", min_Glucose_value)
                     
                     
# shows all the columns that contains NaNs

print (data_frame.loc[:, data_frame.isna().any()])


# shows if columns cointain NaNs with boolean

pandas_check_nans = data_frame.isna().any()
print (pandas_check_nans)

# SO FAR THERE SHOULD NOT BE ANY NaNs IN THE TWO RELEVANT COLUMNS WHICH IS COOL
# TEST STUFF FOR NaNs IS OVER LETS PROCEED


# these lines assign columns to variables for calculation, in this case check which
# columns you need by counting columns in the data source file
# bmi is column number 10 and waist is column number 11

x_BMI = data_frame.iloc[:,10]
y_Waist = data_frame.iloc[:,11]

# counts how many values are in the several columns

# data_frame.count()    or:

print ("__________________________________")
print ()
print ("Number of values in column 'Waist':")
print (len(y_Waist))
print ()
print ("Number of values in column 'BMI':")
print (len(x_BMI))
print ("__________________________________")
print ()





# calculate the mean values of BMI and waist columns via numpy

x_BMI_mean = np.mean(x_BMI)
y_Waist_mean = np.mean (y_Waist)
print ()
print ()
print ("__________________________________")
print ("the mean value of all BMI values is:   " , x_BMI_mean)
print ("the mean value of all Waist values is: " , y_Waist_mean)
print ("__________________________________")
print ()
print ()

#getting the linear regression equation
#numerator is the residual sum of squares
#denominator is the total sum of squares

numerator = 0
denominator = 0

for i in range (len (x_BMI)):
    numerator += (x_BMI[i] - x_BMI_mean)*(y_Waist[i] - y_Waist_mean)
    denominator += (x_BMI[i] - x_BMI_mean)**2
    
m_slope = numerator / denominator
b_y_axis = y_Waist_mean - m_slope * x_BMI_mean

y_linRegLine = m_slope * x_BMI + b_y_axis

print ("__________________________________")
print ()
print ("Number of values in array 'y_linRegLin':")
print (len(y_linRegLine))
print ()
print ("__________________________________")
print ()



# lets try to calculate R² "manually"

# build the sum of "(y_Waist minus y_linRegLine) squared" 

residual_sum_squares = 0
total_sum_squares = 0

for i in range (len (y_Waist)):
    residual_sum_squares += (y_Waist[i] - y_linRegLine[i])**2
    total_sum_squares += (y_Waist[i] - y_Waist_mean)**2
    
r_squared = 1 - (residual_sum_squares / total_sum_squares)



# a class written for the appearance of a print statement

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

# print(color.BOLD + 'Hello World !' + color.END)

print ()
print ()
print ("__________________________________")
print ()
print ("Residual sum of all y-value squares:  ", residual_sum_squares)
print ("Total sum of all y-value squares:     ", total_sum_squares)
print ()
print (color.BOLD + "R², manually with the equation and a for loop:     " + color.END, r_squared)
print ()
print ("__________________________________")


print ("__________________________________")
print ()
print ("numerator:", numerator )
print ("denominator:", denominator)
print ("__________________________________")
print ()

print ("__________________________________")
print ()
print ("slope:", m_slope )
print ("y-axis section:", b_y_axis)
print ("y-axis values of the linear regression line, called predicted value:\n\n", y_linRegLine )
print ("__________________________________")


plt.rcParams['figure.figsize'] = (16,9)
plt.scatter(x_BMI, y_Waist, s = 2)
plt.plot ([min(x_BMI),max(x_BMI)], [min(y_linRegLine),max(y_linRegLine)], color = 'red')
plt.xlabel ('\nBMI\n', fontsize = 14)
plt.ylabel ('Waist\n', fontsize = 14)
plt.title ('Correlation of waist circumference and BMI in 2793 Individuals \n units unknown\n', fontsize = 14)
ax=plt.gca()
plt.text(1.1,0.8,
        'Slope={:.2g}\n\ny-Axis Section={:.2g}\n\nR²={:.2g}'.format(float(m_slope),float (b_y_axis),float(r_squared)),
        transform = ax.transAxes,fontsize = 14,ha = 'center')
ax.tick_params(labelsize = 14)
plt.show()



data_frame.plot.scatter (x = "BMI", 
                         y = "Waist",
                         s = 2, 
                         figsize = (15,10), 
                         title = "Correlation of waist circumference and BMI \n units unknown");


#some seaborn shenanigans

slope, intercept, r_value, pv, se = stats.linregress(data_frame['BMI'],data_frame['Waist'])
sns.regplot(x = "BMI", 
            y = "Waist", 
            data=data_frame, 
            scatter_kws={"color": "blue","s":2}, 
            line_kws={'color': 'red','label':"f(x)={0:.1f}x+{1:.1f}".format(slope,intercept)}).legend(loc="best")






