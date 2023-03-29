# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 12:59:32 2023

@author: szymon.bysko
"""

import pandas as pd
import numpy as np
import seaborn as sns
sns.set()

#%%
df = pd.read_csv('./data/reviews_clean.csv', index_col=0)

#%% plotting categories
df['category'].value_counts().plot(kind='pie')

#%% plotting ratigng frequency
df['rating'].value_counts().sort_index().plot(kind='bar', legend=True, 
                                              title='Frequency')

#%% extract top 3 most rating products
tmp = df.groupby('name').count()['rating'].rename('count').nlargest(3).\
    plot(kind='bar')

#%% extract top 3 high rating products
tmp2 = df.groupby('name').agg('mean').\
    rename(columns={'rating': 'avg_rating'}).\
        nlargest(3, columns='avg_rating').plot(kind='bar')


#%% extract bottom 3 product
tmp3 = df.groupby('name').agg('mean').\
    rename(columns={'rating': 'avg_rating'}).\
        nsmallest(3, columns='avg_rating').plot(kind='bar')
        