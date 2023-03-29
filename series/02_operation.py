# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

# generating data 
np.random.seed(0)

A = np.random.randint(0, 10, 10)
series = pd.Series(A, name='los')

# %%atrributes
series.dtype
series.iloc[1]
series.iloc[-1]
series.index
series.name
series.shape

array_A = series.values


# %% 
N = np.random.randn(10)
M = np.random.randn(10)

series_N = pd.Series(N)
series_M = pd.Series(M)

# %% basic methods

series_N.abs()
series_N.add(series_M)
series_N.subtract(series_M)
series_N.divide(series_M)

series.drop_duplicates()

series[4] = np.nan
series.dropna()

series.idxmax()
series.idxmin()

series.count()

series_N.cumsum()
series_N.cummin()
series_N.cummax()

series.value_counts()

series.sum()
series.std()
series.describe()

# %% histogram
hist_data = pd.Series(np.random.randn(10000))
hist_data.hist(bins=80, color='red')

# %% top n
top_3 = series_N.nlargest(3)

# botton n
bottom_4 = series_N.nsmallest(4)

q_1 = series_N.quantile(0.25)
q_2 = series_N.quantile(0.5)

series_N.round(3)


# %%

shift_1 = series.shift(1)
shift_2_replace_0 = series.shift(2).fillna(0)

#%%
sorted_series = series.sort_values()
sorted_series = series.sort_values(ascending=False)