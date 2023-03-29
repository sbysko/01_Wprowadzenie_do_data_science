# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 14:14:17 2023

@author: szymon.bysko
"""

import pandas as pd
import numpy as np
import seaborn as sns
sns.set()

#%% loading dataset
tips = sns.load_dataset('tips')

#%%
pv = tips.pivot_table(values=['tip', 'total_bill'], index='sex',
                      columns='day', aggfunc='mean')

#%%
tips.pivot_table(values='tip', index='sex', columns='day', aggfunc='max')
tips.pivot_table(values='tip', index='sex', columns='day', aggfunc='min')

#%%
tips.pivot_table(values='tip', index='sex', columns=['smoker','day'],
                 aggfunc='min')
#%%
tips.pivot_table(values='tip', index='sex', columns='day',
                 aggfunc='mean').plot(kind='bar', cmap='viridis', alpha=0.5)


#%%
tips.pivot_table(values='total_bill', index='sex', columns='day',
                 aggfunc='mean').plot(kind='bar', cmap='viridis', alpha=0.5)

#%%
tips.pivot_table(values='total_bill', index='day', columns='size',
                 aggfunc='mean').plot(kind='bar', cmap='viridis', alpha=0.5)
#%%
tips.pivot_table(values='tip', index='time', columns='size',
                 aggfunc='mean').plot(kind='bar', cmap='viridis', alpha=0.5)
#%%
vals = tips[['total_bill','tip']]
vals.corr()