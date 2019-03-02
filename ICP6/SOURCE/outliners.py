import numpy as np
import pandas as pd
train = pd.read_csv('C:/Users/pavan/Downloads/Python_Lesson6/Python_Lesson6/train.csv')

print ("Train data shape:", train.shape)
import matplotlib.pyplot as plt

var ='GarageArea'
data = pd.concat([train['SalePrice'], train[var]], axis=1)
plt.scatter(x=train['GarageArea'], y=train['SalePrice'])
plt.ylabel('Sale Price')
plt.xlabel('Above grade (ground) living area square feet')
plt.show()

from scipy import stats
z = np.abs(stats.zscore(data))
#var ='GarageArea'
#plt.scatter(x=data['GarageArea'], y=data['SalePrice'])
#plt.ylabel('Sale Price')
#plt.xlabel('Above grade (ground) living area square feet')
#plt.show()
#print(z)
#threshold=1
#print(np.where(z>1))


#Q1 = data.quantile(0.1)
#Q3 = data.quantile(1.0)
#IQR = Q3 - Q1
#print(IQR)


#data = data[(z < 1).all(axis=1)]
#boston_df_out = data[~((data < (200)) |(data > (1000))).any(axis=1)]
#data.shape

data_o = data[(z < 2).all(axis=1)]


var ='GarageArea'
plt.scatter(x=data_o['GarageArea'], y=data_o['SalePrice'])
plt.ylabel('Sale Price')
plt.xlabel('Above grade (ground) living area square feet')
plt.show()