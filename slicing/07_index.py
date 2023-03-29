# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

#%%
idx = pd.Index(['8632','3432','5344','4325'])

df = pd.DataFrame(np.random.randn(4,5),
                  index = idx,
                  columns = list('abcde'))

