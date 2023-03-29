# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 13:54:35 2023

@author: szymon.bysko
"""

import numpy as np
import pandas as pd

s = pd.Series(['#sport#good#time', '#workout#free#time','#summer#holliday#hot'],
              name='hashtag')

#%% splitting by hash
s= s.str.split('#')

hash_1 = s.str.get(1)
hash_2 = s.str.get(2)
hash_3 = s.str.get(3)


#%% concatenating by row
df_concat_by_row = pd.concat([hash_1, hash_2, hash_3], ignore_index=True)

string = df_concat_by_row.str.cat(sep=' ')

#%% concatenating by col
df_concat_by_col = pd.concat([hash_1, hash_2, hash_3], axis=1)

#%% other split
split_2 = s.str.split('#', expand=True)
split_2 = split_2.drop(0, axis=1)

#%% replace
s.str.replace('#',' ')
s.str.replace('#','_')
s.str.replace('#','')