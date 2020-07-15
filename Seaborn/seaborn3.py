#!/usr/bin/env python
# coding: utf-8

# In[1]:


import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset('titanic')

sns.set_style('darkgrid')

table = titanic.pivot_table(index=['sex'], columns = ['class'], aggfunc='size')

sns.heatmap(table, annot = True, fmt='d', cmap='YlGnBu', lw=.5, cbar = False)

plt.show()

