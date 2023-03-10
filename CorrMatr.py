import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
from scipy import stats
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


# create the dataframe

data_frame = pd.read_csv(r'C:\Users\Jenny\Desktop\GDBI files\NHANES.txt', delimiter = "\t")

f = plt.figure (figsize = (22,10))
plt.matshow(data_frame.corr(), fignum=f.number)
plt.xticks(range (data_frame.select_dtypes(['number']).shape[1]), data_frame.select_dtypes(['number']).columns, fontsize = 10, rotation =80)
plt.yticks(range (data_frame.select_dtypes(['number']).shape[1]), data_frame.select_dtypes(['number']).columns, fontsize = 10)
cb = plt.colorbar()
cb.ax.tick_params(labelsize = 10)
plt.title ('Correlation Matrix', fontsize = 16);
