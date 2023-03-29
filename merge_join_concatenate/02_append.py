# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 13:45:47 2023

@author: szymon.bysko
"""

import numpy as np
import pandas as pd

#%%
df1 = pd.DataFrame(np.random.rand(10,4), columns=list('abcd'))
df2 = pd.DataFrame(np.random.rand(10,4), columns=list('abcd'))
df3 = pd.DataFrame(np.random.rand(10,4), columns=list('abcd'))

#%%
df = df1.append(df2)
df = df.reset_index()
del df['index']

#%%
df = df1.append(df2).reset_index().drop('index', axis=1)

#%%
df = df1.append(df2, ignore_index=True)