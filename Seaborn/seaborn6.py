#!/usr/bin/env python
# coding: utf-8

# In[2]:


import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset('titanic')

sns.set_style('darkgrid')




sns.countplot(x='class', palette='Set1', data=titanic, ax=ax1)


sns.countplot(x='class', hue='who', palette = 'Set2', data=titanic, ax=ax2)


sns.countplot(x='class', hue='who', palette='Set3', dodge=False, data=titanic, ax=ax3)

ax1.set_title('titanic class')
ax2.set_title('titanic class - who')
ax3.set_title('titanic class - who(stacked)')

plt.show()

