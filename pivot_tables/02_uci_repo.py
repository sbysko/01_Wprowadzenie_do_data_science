# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 14:02:33 2023

@author: szymon.bysko
"""

import pandas as pd
import numpy as np
import seaborn as sns

url=('https://archive.ics.uci.edu/ml/machine-learning-databases/00492/'
     'Metro_Interstate_Traffic_Volume.csv.gz')

#%% loding dataset
metro = pd.read_csv(url, compression='gzip', index_col='date_time', parse_dates=True)
metro = metro.loc['2016-01-01':]

#%% plotting traffic
traffic = metro.iloc[:,-1:]
traffic.plot()
tr = traffic.resample('M').sum()
tr.plot()

#%% pivot tables
pd.pivot_table(data=metro, values='traffic_volume', index='weather_main').plot(kind='bar')
