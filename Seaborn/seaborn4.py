#!/usr/bin/env python
# coding: utf-8

# In[5]:


import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset('titanic')

sns.set_style('darkgrid')


fig = plt.figure(figsize = (15,5))
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)

# 이산형 변수의 분포 - 데이터 분산 미고려
sns.stripplot(x='class', y='age', data=titanic, ax=ax1, hue='sex')

# 이산형 변수의 분포 - 데이터 분산 고려(포인트가 중복되지 않게)
sns.swarmplot(x='class', y='age', data=titanic, ax=ax2, hue='sex')


ax1.set_title('Strip Plot')
ax2.set_title('Strip Plot')

plt.show()

