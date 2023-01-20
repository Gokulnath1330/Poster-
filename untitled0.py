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
