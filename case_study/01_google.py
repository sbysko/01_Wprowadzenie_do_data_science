# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 13:32:13 2023

@author: szymon.bysko
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

#%%
df = pd.read_csv('./data/googleplaystore.csv')

#%% preprocessing
df.info()

col = [col for col in df.columns]

df.columns = [col.replace(' ', '_') for col in df.columns]

df = df.drop(10472)
df = df.reset_index()

df.Reviews = pd.to_numeric(df.Reviews)
#%% categories frequency
tmp = df.groupby('Category').size().rename('Count')
tmp.plot(kind='bar', color='purple', alpha=0.5, title='Categories')


#%% type frequency
tmp2 = df.groupby('Type').size().rename('Freq')
tmp2.plot(kind='pie', cmap='viridis', fontsize=14)

#%%
df = df[['Genres','Rating','Type']]
tmp = df.groupby(['Genres','Type']).agg({'Rating' : ['count', 'mean']})
tmp.columns = ['_'.join(x) for x in tmp.columns.ravel()]
tmp = tmp.sort_values('Rating_count', ascending=False)
tmp = tmp[tmp['Rating_count'] > 100]
tmp.plot(kind='bar',subplots=True,cmap='viridis')

top_5 = tmp.nlargest(5, columns='Rating_count')['Rating_count']
top_5.plot(kind='pie', cmap='viridis')
