# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np


# example 1
s = pd.Series(4)

# example 2
s_def = pd.Series(data=[21, 34, 12], index=['adam', 'tomek', 'pawel'],
                  name='age')

# %% example 3
A = np.random.randn(10)
s = pd.Series(A)

# %% example 4
stocks = {'Apple':'USA', 'CD Projekt':'Poland', 'Amazon':'USA'}
series = pd.Series(stocks, name='country')

# %% example 4
stocks_price = {'Apple': 196, 'CD Projekt':215, 'Amazon':1877}
stocks_price_series = pd.Series(stocks_price, name = 'price')

stocks_price_array = stocks_price_series.values

apple_price = stocks_price_series['Apple']

'Apple' in stocks_price_series


# %% example 5
np.random.seed(0)

A = np.random.randn(20)
s = pd.Series(A)

s[0]
s[1]
s[5:10]
s[:10]
s[5:]