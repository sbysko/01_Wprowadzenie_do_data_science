# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

#%%
s = pd.Series(np.random.randn(20))

df = pd.DataFrame(np.random.randn(31, 5),
                  columns = list('abcde'),
                  index = pd.date_range(start='2019-01-01', periods=31))

#%% series
out = s[s > 0]
out = s.where(s>0)


#%% dataframe
out = df[df > 0]
out = df.where(df > 0)

out = df.where( df > 0, 0)

out = df.where( df > 0, 0).where(df < 1, 1)

#%%
df = df.where( df > 0, 0).where(df < 1, 1)
