# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 13:42:16 2023

@author: szymon.bysko
"""

from selenium import webdriver
import pandas as pd

#%%
df = pd.read_html('./data/small.html', header=0, index_col=0)[0]

#%%
df_= pd.read_html('https://www.biznesradar.pl/gielda/indeks:WIG20')[0]

#%%
driver = webdriver.Chrome(chromedriver)
driver.implicitly_wait(30)


driver.get('https://stooq.pl/t/?i=516')
#df=pd.read_html(driver.find_element_by_id("history_table").get_attribute('outerHTML'))[0]



#%%
df___= pd.read_html('https://finance.yahoo.com/crypto')



