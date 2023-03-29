# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 14:05:57 2023

@author: szymon.bysko
"""

import numpy as np
import pandas as pd

string = 'workout summer good free holiday time time hot'

#%% splitting string
split = string.split(' ')

s = pd.Series(split)

#%% contains method
s.str.contains(r'[0-9]')
s.str.contains(r'[rg]')
s[s.str.contains(r'[rg]')]