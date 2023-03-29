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

#%%
"""
SELECT *
FROM retail;
"""
query = retail

#%%
"""
SELECT Quantity, UnitPrice, CustomerID
FROM retail;
"""
query = retail[['Quantity','UnitPrice','CustomerID']]


#%%
"""
SELECT Quantity, UnitPrice, CustomerID
FROM retail;
LIMIT 10
"""
query = retail[['Quantity','UnitPrice','CustomerID']][:10]
query_ = retail[['Quantity','UnitPrice','CustomerID']].head(10)

#%%
"""
SELECT *
FROM retail;
WHERE CustomerID = '17850'
"""
query = retail[retail['CustomerID'] == '17850']
query_ = retail.query("CustomerID == '17850'")
