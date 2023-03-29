# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 12:08:34 2023

@author: szymon.bysko
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#%%
df = pd.read_csv('./data/ten.csv', index_col=0)
df.columns = ['Open', 'High', 'Low', 'Close', 'Volume']
clean_price = df[['Open', 'High', 'Low', 'Close']]

#%% computing correlation matrix
corr_matrix = clean_price.corr()

#%% corr between series
df['Open'].corr(df['Close'])

#%% plot correlation matrix using matplotlib
#plt.matshow(corr_matrix)
sns.heatmap(corr_matrix)