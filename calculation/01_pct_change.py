# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 14:08:48 2023

@author: szymon.bysko
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#%%
df = pd.read_csv('./data/ten.csv', index_col=0)
df.columns = ['Open', 'High', 'Low', 'Close', 'Volume']


#%% pct_change daily
df['Daily_Chagne'] = df['Close'].pct_change()



#%% pct_change 5 days
df['5_Daily_Chagne'] = df['Close'].pct_change(periods=5)

#%% pct_change Close to Open
df['Close_top_Open'] = df[['Open', 'Close']].pct_change(axis=1).drop('Open', axis = 1)

#%%
clean_price = df[['Open', 'High', 'Low', 'Close']]
daily_changes = clean_price.pct_change()