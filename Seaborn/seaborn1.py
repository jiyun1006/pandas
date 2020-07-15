#!/usr/bin/env python
# coding: utf-8

# In[7]:


import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset('titanic')

print(titanic.head())
# print('\n')
# print(titanic.info())

sns.set_style('darkgrid')

fig = plt.figure(figsize=(15, 5))
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)

# 선형회귀선 (fit_reg=True)
sns.regplot(x='age', y='fare', data=titanic, ax=ax1)

sns.regplot(x='age', y='fare', data=titanic, ax=ax2, fit_reg=False, color='orange')

plt.show()
