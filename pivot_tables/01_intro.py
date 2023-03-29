# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 14:12:06 2023

@author: szymon.bysko
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

#%% loading dataset
tit = sns.load_dataset('titanic')

#%% grouping by sex
tit.groupby('sex').size().plot(kind='bar', alpha=0.5)
tit.groupby(['sex','survived']).size()

#%% grouping by classes
tit.groupby(['class']).size().plot(kind='bar', alpha=0.5)
tit.groupby(['class']).mean()['survived'].plot(kind='bar', alpha=0.5)

r = pd.pivot_table(data=tit, values='survived', index='sex', columns='class', aggfunc='count')

#%% making variable age categorial and grouping by age
tit['age_bin'] = pd.cut(x=tit['age'], bins=[0, 18, 80])
pv = pd.pivot_table(data=tit, values='survived', index='age_bin', columns='class', aggfunc='count')

#%% making subplots
fig, ax = plt.subplots(1, 2, sharey=True)
tit.groupby(['sex','survived']).size()['male'].plot(ax=ax[0], kind='bar')
tit.groupby(['sex','survived']).size()['female'].plot(ax=ax[1], kind='bar')

ax[0].legend('male')
ax[1].legend('female')

#%% pivoting table
r = pd.pivot_table(data=tit, values='age', index='survived', columns='sex', aggfunc='count')
r.plot(subplots=True, kind='bar',sharey=True, layout=(1,2))

#%% pivoting table
z = pd.pivot_table(data=tit, index='sex', columns='class', aggfunc={'survived':sum, 'fare':'mean', 'age':'mean'})

#%% pivoting table

#%% making categorical column from continuos variable
