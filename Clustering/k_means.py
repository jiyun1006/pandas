import pandas as pd
import matplotlib.pyplot as plt

'''
STEP1 데이터 준비
'''

uci_path = 'https://archive.ics.uci.edu/ml/machine-learning-databases/00292/Wholesale%20customers%20data.csv'
df = pd.read_csv(uci_path, header=0)

'''
STEP2 데이터 탐색
'''

print(df.head())
print('\n')

print(df.info())
print('\n')

'''
STEP3 데이터 전처리
'''

X = df.iloc[:, :]
print(X[:5])
print('\n')

from sklearn import preprocessing

X = preprocessing.StandardScaler().fit(X).transform(X)

print(X[:5])

'''
STEP4 k-means 군집 모형
'''

from sklearn import cluster

kmeans = cluster.KMeans(init='k-means++', n_clusters=5, n_init=10)

kmeans.fit(X)

cluster_label = kmeans.labels_
print(cluster_label)
print('\n')

df['Cluster'] = cluster_label
print(df.head())

# df.plot(kind='scatter', x='Grocery', y='Frozen', c='Cluster', cmap='Set1', colorbar=False, figsize=(10, 10))
# df.plot(kind='scatter', x='Milk', y='Delicassen', c='Cluster', cmap='Set1', colorbar=True, figsize=(10, 10))
# plt.show()
# plt.close()

mask = (df['Cluster'] == 0) | (df['Cluster'] == 4)
ndf = df[~mask]

ndf.plot(kind='scatter', x='Grocery', y='Frozen', c='Cluster', cmap='Set1', colorbar=False, figsize=(10, 10))
ndf.plot(kind='scatter', x='Milk', y='Delicassen', c='Cluster', cmap='Set1', colorbar=True, figsize=(10, 10))
plt.show()
plt.close()