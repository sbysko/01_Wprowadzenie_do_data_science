# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 13:27:06 2023

@author: szymon.bysko
"""

import pandas as pd

# %%

df = pd.read_csv('./data/apple.csv', sep=',', index_col=0)

#%%
df_ = pd.read_csv('./data/apple.csv', sep=',', index_col=0, skiprows=10)

#%%
df_ = pd.read_csv('./data/apple.csv', sep=',', index_col=0, nrows=100)

#%%
df = pd.read_csv('./data/reviews_clean.csv', sep=',', index_col=0)