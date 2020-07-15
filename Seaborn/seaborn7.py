#!/usr/bin/env python
# coding: utf-8

# In[1]:


import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset('titanic')

sns.set_style('darkgrid')

j1 = sns.jointplot(x='fare', y='age', data=titanic)

j2 = sns.jointplot(x='fare', y='age', kind='reg', data=titanic)

j3 = sns.jointplot(x='fare', y='age', kind='hex', data=titanic)

j4 = sns.jointplot(x='fare', y='age', kind='kde', data=titanic)

j1.fig.suptitle('titanic fare - scatter', size =15)
j2.fig.suptitle('titanic fare - reg', size =15)
j3.fig.suptitle('titanic fare - hex', size =15)
j4.fig.suptitle('titanic fare - ked', size =15)
plt.show()

