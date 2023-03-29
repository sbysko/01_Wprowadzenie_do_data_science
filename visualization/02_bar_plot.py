# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 13:45:02 2023

@author: szymon.bysko
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

#%%
df = pd.DataFrame(np.random.randn(100,4),
                  columns=list('ABCD'))

#%% bar plot
bar_data = df.cumsum().iloc[-1].apply(abs)

bar_data.plot(kind='bar', title='Random generated data',color='green', alpha=0.3)

#%% multiple bar plot vertical
df_bar = pd.DataFrame(np.random.rand(10,4),
                  columns=list('ABCD'))

df_bar.plot(kind='bar', cmap='viridis', title='Multiple bar plot', alpha=0.7)
df_bar.plot.bar(cmap='viridis', title='Multiple bar plot', alpha=0.7)

#%%muliple bar plot horizontal
df_bar.plot.barh(cmap='hot', title='Multiple bar plot', alpha=0.7)

#%% stacked bar plot vertical
df_bar.plot.bar(cmap='viridis', title='Multiple bar plot', alpha=0.7, stacked=True)

#%% stacked bar plot horizontal
df_bar.plot.barh(cmap='viridis', title='Multiple bar plot', alpha=0.7, stacked=True)