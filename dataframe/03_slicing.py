# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

#%% importing dataset
df = pd.read_csv('./data/aapl_us_d.csv', index_col=0)

#%% select only first n rows
df.iloc[:5]
df.iloc[10:20]
df.iloc[10:]
df.iloc[[1,4,10], [0, 4]]
df.iloc[::3] # co 3 wiersz


#%% select only first n columns
df.iloc[:, :2]
df.iloc[:5, :2]
df.iloc[5:10, 3:]
df.iloc[:,::2] #co 2 kolumna
