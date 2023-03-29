# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 13:37:10 2023

@author: szymon.bysko
"""

import pandas as pd
#%%
df = pd.read_excel('./data/companies.xlsx', na_values='?', index_col=0)

#%%
df_msft = pd.read_excel('./data/companies.xlsx', na_values='?', index_col=0,
                        sheet_name='microsoft')

df_google = pd.read_excel('./data/companies.xlsx', na_values='?', index_col=0,
                        sheet_name='google')