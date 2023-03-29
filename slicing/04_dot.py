# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

#%%
df = pd.DataFrame(np.random.randn(20, 5),
                  columns = list('abcde'),
                  index = list('abcdefghijklmnoprtst'))

#%%
col_a = df.a

mask = df.a > 0
out = df[mask]

out = df[df.a > 0]

#%%
mask = (df.a > 0) & (df.c > 0)
out = df[mask]

#%%

mask = (df.a > 0) | (df.b > 0)
out = df[mask]