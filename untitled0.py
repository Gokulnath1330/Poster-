# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 19:56:07 2023

@author: GOKULNATH
"""
# It is to understand database easier
import wbgapi as wb
# Implementation of pandas function
import pandas as pd
from scipy.optimize import curve_fit
# Implementation of clustering as kmeans
from sklearn.cluster import KMeans
# Implementation of matplotlib function
import matplotlib.pyplot as plt
# Implementation of machine learning function
import sklearn
import seaborn as sns
# Implementation of Iteration function
import itertools as iter
from sklearn.datasets import make_blobs
# Implementation of numpy function
from numpy import array, exp
report=pd.read_csv(r"E:\poster\World_Data_Indicators.csv")
report.head()
report.info()
report.shape
report.describe()

#Indicators to be chosen for analysis
economy = ['NE.IMP.GNFS.ZS','NY.GDP.MKTP.CD']
country = ["JPN","AUS",'BMU','LUX','IND','BRA','ARG','ESP','GBR','CHL']
climate=['EG.CFT.ACCS.RU.ZS','EG.CFT.ACCS.UR.ZS']
gokul_economy  = wb.data.DataFrame(economy, country, mrv=7)
gokul_climate  = wb.data.DataFrame(climate, country, mrv=7)
gokul_economy.columns = [f.replace('YR','') for f in gokul_economy.columns]      
gokul_economy=gokul_economy.stack().unstack(level=1)                             
gokul_economy.index.names = ['Country_Name', 'Year']                           
gokul_economy.columns                                                     
gokul_economy.fillna(0)
gokul_economy.head()
gokul_climate.columns = [f.replace('YR','') for f in gokul_climate.columns]      
gokul_climate=gokul_climate.stack().unstack(level=1)                             
gokul_climate.index.names = ['Country_Name', 'Year']                           
gokul_climate.columns                                                     
gokul_climate.fillna(0)
gokul_climate.head()
# Rest index is used to reset back to the default
economy1=gokul_economy.reset_index()
# replace all elements with Zero
economy2=economy1.fillna(0)
climate1=gokul_climate.reset_index()
climate2=climate1.fillna(0)

# It is used to merge data
merged_data = pd.merge(economy2, climate2)
merged_data.head()
merged_data1 = merged_data.iloc[:,2:]
merged_data.iloc[:,2:] = (merged_data1-merged_data1.min())/ (merged_data1.max() 
                                                        - merged_data1.min())
merged_data.head()
merged_data2 = merged_data.drop('Country_Name', axis = 1)
# Using clustering function
k_clustering = KMeans(n_clusters=3, init='k-means++', random_state=0).fit(merged_data2)

#Clean fuels access and technologies access clustering in rural areas
sns.scatterplot(data=merged_data, x="Country_Name", y="EG.CFT.ACCS.RU.ZS",
                hue=k_clustering.labels_)
plt.legend(loc='lower right')
plt.show()

# Association between Total imports and Total GDP of a country(Brazil)
g=merged_data[(merged_data['Country_Name']=='BRA')]
data = g.values
x, y = data[:, 2], data[:, 3]
plt.scatter(x, y,color="green")
plt.title('GDP vs Total Imports')
plt.ylabel('Total Imports')
plt.xlabel('Total GDP of a country')
plt.show()


#curve_fit function
k=merged_data[(merged_data['Country_Name']=='LUX')]
gokul1 = k.values
x, y = gokul1[:, 2], gokul1[:, 3]

# To define a function use def 
def functn(x, a, b, c):
    return a*x**2+b*x+c
param, covar = curve_fit(functn, x, y)
param, _ = curve_fit(functn, x, y)
print("Function Covariance ->", covar)
print("Function Parameters ->", param)

a, b, c = param[0], param[1], param[2]
y_fit =a*x**2+b*x+c
import warnings

with warnings.catch_warnings(record=True):
    plt.plot(x, y_fit, label="y=a*x**2+b*x+c",color="green")
    plt.grid(True)
    plt.plot(x, y, 'bo', label="Original Y",color="red")
    plt.ylabel('Total Imports')
    plt.title('GDP vs Total Imports')
    plt.xlabel('Total GDP of a country')
    plt.legend(loc='best', fancybox=True, shadow=True)
    plt.show() 
    m=merged_data[(merged_data['Country_Name']=='IND')]
gokul2 = m.values
x, y = gokul2[:, 2], gokul2[:, 3]

# To define a function use def 
def functn(x, a, b, c):
    return a*x**2+b*x+c
# Implementation of parameter and covariance function
param, covar = curve_fit(functn, x, y)
param, _ = curve_fit(functn, x, y)
print("Function Covariance ->", covar)
print("Function Parameters ->", param)

a, b, c = param[0], param[1], param[2]
y_fit =a*x**2+b*x+c

# It is to warn the condition normally doesn't warn raising an exception
import warnings
with warnings.catch_warnings(record=True):
    plt.plot(x, y_fit, label="y=a*x**2+b*x+c",color="green")
    plt.grid(True)
    plt.plot(x, y, 'bo', label="Original Y",color="red")
    plt.ylabel('Total Imports')
    # To display the title
    plt.title('GDP vs Total Imports')
    # To display th label
    plt.xlabel('Total GDP of a country')
    plt.legend(loc='best', fancybox=True, shadow=True)
    plt.show() 
    
    l=merged_data[(merged_data['Country_Name']=='BRA')]
gokul3 = l.values
x, y = gokul3[:, 2], gokul3[:, 3]

# To define a function use def 
def functn(x, a, b, c):
    return a*x**2+b*x+c
param, covar = curve_fit(functn, x, y)
param, _ = curve_fit(functn, x, y)
print("Function Covariance ->", covar)
print("Function Parameters ->", param)

a, b, c = param[0], param[1], param[2]
y_fit =a*x**2+b*x+c

# To  warn programmers about change in language
import warnings

with warnings.catch_warnings(record=True):
    plt.plot(x, y_fit, label="y=a*x**2+b*x+c",color="green")
    plt.grid(True)
    plt.plot(x, y, 'bo', label="Original Y",color="red")
    plt.ylabel('Total Imports')
    # To display the title
    plt.title('GDP vs Total Imports')
    # To label the parts 
    plt.xlabel('Total GDP of a country')
    # To display the symbols on graph 
    plt.legend(loc='best', fancybox=True, shadow=True)
    # To show the plot
    plt.show() 
    
    