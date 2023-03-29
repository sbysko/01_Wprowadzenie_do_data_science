# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 14:11:40 2023

@author: szymon.bysko
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

#%%
ts = pd.Series(np.random.randn(1000),
               index=pd.date_range('2019-01-01', periods=1000))

#%%
ts.cumsum().plot()

#%%
ts.cummin().plot()

#%%
ts.cummax().plot()

#%%
df = pd.DataFrame(np.random.randn(1000,5),
                  index=pd.date_range('2019-01-01', periods=1000),
                  columns=list('ABCDE'))


#%%
df.cumsum().plot()

#%%
df['A'].plot()

#%%
abs(df.iloc[5]).plot(kind='bar', title='Wykres')