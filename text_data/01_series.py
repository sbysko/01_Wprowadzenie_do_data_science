# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

s = pd.Series(['Appple', '   Microsoft', np.nan, '  Google','Amazon'],
               name='stock')

#%%
s = s.str.strip()

#%%
s = s.str.upper()

#%%
s = s.str.lowe()

#%%
s= s.str.len()

#%%
df = pd.DataFrame(np.random.randn(10,2),
                  columns=['                       ID User      ','     Price       '])

#%%
df.columns = df.columns.str.strip()
df.columns = df.columns.str.replace(' ', '_')