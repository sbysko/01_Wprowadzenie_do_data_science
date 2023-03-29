# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

# %% generating data
np.random.seed(0)

s = pd.Series(np.random.randn(20))

# %% aggregate

minimum = s.aggregate(min)
maximum = s.aggregate(max)

suma = s.aggregate(sum)

means = s.aggregate(np.mean)
std = s.aggregate(np.std)

# %%
stats = s.aggregate(['min', 'max','sum','mean'])

stats_np = s.aggregate([np.mean, np.std, np.median])