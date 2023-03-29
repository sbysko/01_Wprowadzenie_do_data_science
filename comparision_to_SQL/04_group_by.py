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


#%% groupby
"""
SELECT CustomerID, count(*)
FROM retail
Group By CustomerID
"""

cust_id = retail.groupby('CustomerID').size()
country = retail.groupby('Country').size()
country.plot(kind='bar')

#%% compute new colls Revenue
retail['Revenue']  = retail['Quantity'] * retail['UnitPrice']


#%%
"""
SELECT CustomerID, avg(Revenue), count(*)
FROM retail
Group By CustomerID

"""
result = retail.groupby('CustomerID').agg({'Revenue':np.mean,
                        'CustomerID':np.size}).rename(columns=
                       {'Revenue':'Average_Revenue',
                        'CustomerID':'Count_Customer'})

#%% making InvoiceDateDay column
retail['InvoiceDay'] = retail['InvoiceDate'].dt.day
query = retail.groupby('InvoiceDay').agg({'Revenue' : sum})
query.plot(kind='bar', color='black', alpha=0.5, title='Sales by day')

#%% grouping by  InvoiceDateDay column
mask = (retail['InvoiceDate'] > '2010-12-09') & (retail['InvoiceDate'] < '2010-12-10')
day_9 = retail[mask]
day_9['Hour'] = day_9['InvoiceDate'].dt.hour

query = day_9.groupby('Hour').agg({'Revenue' : sum})
query.plot(kind='bar', color='blue', alpha=0.5, title='Sales by hour')

