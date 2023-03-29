# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 11:26:23 2023

@author: szymon.bysko
"""

import pandas as pd
import numpy as np

df = pd.read_csv('./data/cdr_d.csv', index_col=0)

close_price = df['Zamkniecie']

#export to csv
close_price.to_csv('./data/close_price.csv', header=['close'])


#export to json
close_price.to_json('./data/close.json')

close_price_dict = close_price.to_dict()

clipboard_df = pd.read_clipboard()

clipboard_df.to_csv('./data/clip.csv')