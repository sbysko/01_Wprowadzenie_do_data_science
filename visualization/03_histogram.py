# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 13:53:05 2023

@author: szymon.bysko
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()


#%%
df = pd.DataFrame(np.random.rand(100000))

#%% histogram
df.hist(bins=40)

df.plot(kind='hist', bins=40)

#%% creating dataset, normal
df = pd.DataFrame(np.random.randn(100000))
df.hist(bins=100, color='red',alpha=0.5)

#%% multiple histogram
df = pd.DataFrame({'mu_0_sigma_1' : np.random.randn(100000),
                   'mu_1_sigma_2' : 2 * np.random.randn(100000) + 1,
                   'mu_8_sigma_3' : 3 * np.random.randn(100000) + 8})

df.plot.hist(bins=100, cmap='viridis', alpha=0.5, title='Different Normal Distribution')


#%% cummulative plot
df['mu_8_sigma_3'].plot.hist(bins=100, cumulative=True, color='green', alpha=0.5)


#%%
df.hist(sharex=True, sharey=True, bins=100, color='green', alpha=0.5)