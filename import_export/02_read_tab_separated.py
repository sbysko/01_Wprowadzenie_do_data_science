# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 13:34:53 2023

@author: szymon.bysko
"""


import pandas as pd

df = pd.read_csv('./data/apple.tsv', sep='\t', index_col=0)