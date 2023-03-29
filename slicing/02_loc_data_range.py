# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

#%%
df = pd.DataFrame(np.random.randn(31, 5),
                  columns = list('abcde'),
                  index = pd.date_range(start='2019-01-01', periods=31))

#%%
idx = df.index

day = df.loc['2019-01-02'] # series
week = df.loc['2019-01-01':'2019-01-07']

after_15 = df.loc['2019-01-15':]
before_15 = df.loc[:'2019-01-15']