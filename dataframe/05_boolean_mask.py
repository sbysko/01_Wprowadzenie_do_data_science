# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

#%% importing dataset
df = pd.read_csv('./data/aapl_us_d.csv', index_col=0)
df.columns = ['Open', 'High', 'Low', 'Close', 'Volume']

#%% creating mask
df_bool = df > 150
df_ = df[df_bool]

#%%
df_ = df[df > 150]

#%%
df_2019 = df['2019-01-01':]

#%%
df_jan_2019 = df['2019-01-01': '2019-01-31']

#%%
df_jan_2019.query('Close > 160')
