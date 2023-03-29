# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

df_1 = pd.DataFrame(np.random.randn(10,3), columns=list('ABC'))
df_2 = pd.DataFrame(np.random.randn(10,3), columns=list('ABC'))

#%%
df_1 + df_2

df_1 - df_2

df_1 * df_2

df_1 / df_2

df_1 ** 2 # potęgowanie

(df_1 ** 2) + df_2

np.exp(df_1)
