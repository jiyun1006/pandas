import pandas as pd
import numpy as np

'''
STEP1 데이터 준비 / 기본설정
'''
uci_path = 'https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data'
df = pd.read_csv(uci_path, header=None)

df.columns = ['id', 'clump', 'cell_size', 'cell_shape', 'adhesion', 'epithlial', 'bare_nuclei', 'chromatin',
              'normal_nucleoli', 'mitoses', 'class']

pd.set_option('display.max_columns', 15)

'''
STEP2 데이터 탐색
'''

# print(df.head())
# print('\n')
#
# print(df.info())
# print('\n')
#
# print(df.describe())

print(df['bare_nuclei'].unique())
print('\n')

df['bare_nuclei'].replace('?', np.nan, inplace=True)
df.dropna(subset=['bare_nuclei'], axis=0, inplace=True)
df['bare_nuclei'] = df['bare_nuclei'].astype('int')

'''
STEP3 데이터 셋 구분 
'''

X = df[['clump', 'cell_size', 'cell_shape', 'adhesion', 'epithlial', 'bare_nuclei', 'chromatin', 'normal_nucleoli',
        'mitoses']]
y = df['class']

from sklearn import preprocessing

X = preprocessing.StandardScaler().fit(X).transform(X)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=10)

'''
STEP4 Decision Tree 분류 모형
'''

from sklearn import tree

tree_model = tree.DecisionTreeClassifier(criterion='entropy', max_depth=5)

tree_model.fit(X_train, y_train)

y_hat = tree_model.predict(X_test)

print(y_hat[0:10])
print(y_test.values[0:10])
print('\n')


from sklearn import metrics
tree_matrix = metrics.confusion_matrix(y_test, y_hat)
print(tree_matrix)
print('\n')

tree_report = metrics.classification_report(y_test, y_hat)
print(tree_report)