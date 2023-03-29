# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 14:27:00 2023

@author: szymon.bysko
"""

import pandas as pd
import numpy as np

url=('https://archive.ics.uci.edu/ml/machine-learning-databases/00352/'
     'Online%20Retail.xlsx')

retail = pd.read_excel(url)

#%% exploring dataset
retail.info()
cols = [col for col in retail.columns]
retail.head()
retail.tail()
#%% preprocessing
# drop rowis with null
retail = retail[retail['CustomerID'].notnull()]

# convert type to string
retail['CustomerID'] = retail['CustomerID'].apply(lambda x: str(int(x)))

# exclude Quantity less than zero
retail = retail[retail['Quantity'] > 0]

#%% and
"""
SELECT *
FROM retail;
WHERE CustomerID='17850' and UnitPrice > 5;
"""

query = retail[(retail['CustomerID'] == '17850') & (retail['UnitPrice'] > 5)]
query_ = retail.query("CustomerID == '17850' and UnitPrice > 5")

#%%
"""
SELECT Quantity, UnitPrice, CustomerID
FROM retail;
WHERE CustomerID='17850' and Country='France';
"""
query = retail[(retail['CustomerID'] == '17850') | (retail['Country'] == 'France')]
query_ = retail.query("CustomerID == '17850' or Country == 'France'")



