# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 13:56:07 2023

@author: szymon.bysko
"""

import pandas as pd
import numpy as np
import wget
import os, zipfile
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

#%%
url = ('https://archive.ics.uci.edu/ml/machine-learning-databases/00275/'
       'Bike-Sharing-Dataset.zip')

wget.download(url)

#%% preprocessing
z = zipfile.ZipFile('Bike-Sharing-Dataset.zip')
z.extractall('./data')

#%%
day = pd.read_csv('./data/day.csv', index_col='dteday')
hour = pd.read_csv('./data/hour.csv', index_col='dteday')

#%%
hour.groupby('weekday').size().plot(kind='bar')
hour.groupby('hr').size().plot(kind='bar')
