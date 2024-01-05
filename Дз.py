#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Получаем уникальные значения столбца 'whoAmI'
unique_values = np.unique(data['whoAmI'])

# Создаем пустой DataFrame с нулями и именами колонок по уникальным значениям
one_hot_encoded = pd.DataFrame(0, columns=unique_values, index=np.arange(len(data)))

# Присваиваем 1 для каждого значения в соответствующей колонке
for i, val in enumerate(data['whoAmI']):
    one_hot_encoded.loc[i, val] = 1

print(one_hot_encoded.head())

