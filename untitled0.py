# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 14:47:42 2023

@author: ms23agu
"""
import pandas as pd 
import matplotlib.pyplot as plt 

data = pd.read_csv ('VOD_ann.csv')

returns = data['ann_return']

plt.hist(data, bins=100)
plt.xlabel ('returns')
plt.ylabel ('year')
plt.title ('Yearly returns')

custom_xticks = [ 1981, 1982, 1983, 2020, 2021]
plt.xticks (custom_xticks)

plt.show()
