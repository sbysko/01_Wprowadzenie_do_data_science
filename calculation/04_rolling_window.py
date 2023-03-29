# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 12:21:44 2023

@author: szymon.bysko
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

#%%
df = pd.read_csv('./data/ten.csv', index_col=0)
df.columns = ['Open', 'High', 'Low', 'Close', 'Volume']
clean_price = df[['Open', 'High', 'Low', 'Close']]
volume = df[['Volume']].copy()

#%% Series
cum_vol = volume.cumsum()


#%% plot cumulative sum of volume
cum_vol.plot()

#%% plot moving averagee
close = df['Close']
close_rol_avg = close.rolling(window=30).mean()
close.plot()
close_rol_avg.plot(style='k--')

#%% moving averages

close.plot(color='black')

for i in [5,8,12, 60, 65, 70]:
    close_rol_avg = close.rolling(window=i).mean()
    close_rol_avg.plot(alpha=0.5)



#%% simple strategy
close.plot(color='black')

for i in [5]:
      close_rol_min = close.rolling(window=i).min()
      close_rol_min.plot()
      close_rol_max = close.rolling(window=i).max()
      close_rol_max.plot()

#%% dataframe
clean_price.rolling(window=20).mean().plot()
close.plot(color='black')

#%% dataframe std
close.rolling(window=15).std().plot()
close.plot(color='black')

#%% dataframe subplots
clean_price.rolling(window=20).mean().plot(subplots=True)

#%% apply, custom indicator
xxx = close.rolling(window=10).apply(lambda x: (x-x.mean()).mean())
xxx.plot()

