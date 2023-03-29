# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 11:34:50 2023

@author: szymon.bysko
"""


import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.randn(10, 4),
                  columns=['one','two','three','four'])

#%%
for row in df.values: 
    i = np. random.choice([0,1,2,3])
    row[i] = np.nan
    
#%%
for row in df.values: 
    switch = np.random.choice([0,1])
    if switch:
        i = np. random.choice([0,1,2,3])
        row[i] = np.nan
        
#%%
df.isnull()
df[df.isnull()]
df['one'].isnull()
df[~df['one'].isnull()]

#%%
df.notnull()
df[df.notnull()]
df['one'].notnull()
df[df['one'].notnull()]

#%%
df['five'] = np.nan

del df['five']