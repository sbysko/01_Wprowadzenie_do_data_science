# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 11:47:14 2023

@author: szymon.bysko
"""

import pandas as pd
import numpy as np

#%%
df = pd.read_csv('./data/Consumer_Reviews_Amazon.csv', index_col=0)

#%%
df.describe()

#%%
for col in df.columns:
    print(col)
    
df.columns = [col.replace('.','_') for col in df.columns]

#%%
df = df[['name','primaryCategories','reviews_rating','reviews_text']]

#%%
df.columns = ['name', 'category', 'rating', 'text']
df.info()
df.describe()


#%%
df.to_csv('./data/reviews_clean.cvs')
