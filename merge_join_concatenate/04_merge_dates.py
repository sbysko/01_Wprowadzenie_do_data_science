# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 14:14:03 2023

@author: szymon.bysko
"""

import numpy as np
import pandas as pd

d1 = {'date' : ['2019-01-01','2019-01-01','2019-01-02','2019-01-02'],
      'id' : ['0001', '0002', '0003', '0004'],
      'product_id' : ['0343','0523','0151', '0022']}

d2 = {'date' : ['2019-01-01','2019-01-02','2019-01-02','2019-01-03'],
      'id' : ['0001', '0002', '0003', '0004'],
      'price' : ['99','149','59', '199']}

left = pd.DataFrame(d1)
right = pd.DataFrame(d2)

#%% inner
df_inner = pd.merge(left, right, how='inner',on=['date', 'id'])


#%% outter
df_outer = pd.merge(left, right, how='outer',on=['date', 'id'])

#%% left
df_left = pd.merge(left, right, how='left',on=['date', 'id'])


#%% right
df_right = pd.merge(left, right, how='right',on=['date', 'id'])