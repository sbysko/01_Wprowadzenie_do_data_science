# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

#%%
df = pd.DataFrame(np.random.randn(20, 5),
                  columns = list('abcde'),
                  index = list('abcdefghijklmnoprtst'))

#%%
# iloc[index_row, index_column]

col_1 = df.iloc[:,0]
col_1_2 = df.iloc[:,:2]
col_a_b = df.iloc[:,[0,1]]

col_last = df.iloc[:,-1]
col_last = df.iloc[:,4]

col_by_2 = df.iloc[:,::2]
col_by_2 = df.iloc[:,1::2]


#%%
row_1 = df.iloc[0, :] #series
row_1 = df.iloc[[0], :] #dataframe
row_1_5_6 = df.iloc[[0,5,6],:]

row_last = df.iloc[[-1],:]

row_by_2 = df.iloc[3::2,:]

#%%

df_ = df.iloc[[0,-1],[0, 4]]
df_ = df.iloc[2:8,1:]