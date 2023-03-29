# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

#%%
df_raw = pd.read_clipboard()

#%%
columns = [col for col in df_raw.columns]

#%%
df = df_raw.drop(['Czas ','1r 3m'], axis = 1)

#%%
df['Wolumen '] = df['Wolumen '].apply(lambda s: s.replace(' ',''))\
    .apply(lambda s: int(s))

#%%

df['Obrót '] = df['Obrót '].apply(lambda s: s.replace(' ',''))\
    .apply(lambda s: int(s))

#%%
df['Udział '] = df['Udział '].apply(lambda s: s.replace('%',''))\
    .apply(lambda s: float(s))

#%%
df['Zmiana % '] = df['Zmiana % '].apply(lambda s: s.replace('%',''))\
    .apply(lambda s: s.replace('(','')).apply(lambda s: s.replace(')',''))\
        .apply(lambda s: float(s))
        
#%%
df.columns = df.columns.str.strip()
        
