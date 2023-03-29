# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 12:50:26 2023

@author: szymon.bysko
"""

import numpy as np
import pandas as pd
import pytz

#%%
rng = pd.date_range('2019-01-01', periods=100)
rng = pd.date_range('2019-01-01', periods=100, freq='S')
rng = pd.date_range('2019-01-01', periods=100, freq='M')
rng = pd.date_range('2019-01-01', periods=100, freq='MS')
rng = pd.date_range('2019-01-01', periods=100, freq='3M')
rng = pd.date_range('2019-01-01', periods=100, freq='H')
rng = pd.date_range('2019-01-01', periods=100, freq='6H')
rng = pd.date_range('2019-01-01', periods=100, freq='B')
rng = pd.date_range('2019-01-01', periods=100, freq='Q')
rng = pd.date_range('2019-01-01', periods=100, freq='QS')
rng = pd.date_range('2019-01-01', periods=100, freq='MIN')
rng = pd.date_range('2019-01-01', periods=100, freq='T')
rng = pd.date_range('2019-01-01', periods=100, freq='W')
rng = pd.date_range('2019-01-01', periods=100, freq='A')
rng = pd.date_range('2019-01-01', periods=100, freq='QS-FEB')
rng = pd.date_range('2019-01-01', periods=100, freq='W-MON')
rng = pd.date_range('2019-01-01', periods=100, freq='2H30T')

#%% getting all available time zone
times_zones = list(pytz.all_timezones)
europe = [tz for tz in times_zones if tz.startswith('Europe')]


#%% date range with Warsaw Time
rng = pd.date_range('2019-01-01', periods=100, tz='Europe/Warsaw', freq='MS')

us = rng.tz_convert(tz='US/Central')

#%% 
rng = pd.date_range('2019-01-01', periods=100, tz='Europe/Warsaw', freq='MIN')
ts = pd.Series(np.random.randn(100), index=rng)
ts_period = ts.to_period()

ts_period.plot()
#%% resample method
ts_sample = ts.resample('5MIN').sum()

ts_sample.plot()
