import pandas as pd
import seaborn as sns

'''
STEP1 데이터 탐색
'''

df = sns.load_dataset('titanic')

'''
STEP2 데이터 탐색
'''

# 열 개수가 적은 'deck'열 제거, 중복되는 열인 'embark_town'도 제거.
rdf = df.drop(['deck', 'embark_town'], axis=1)
print(rdf.columns.values)
print('\n')

# 'age'에 결측치있는 행을 제거
rdf = rdf.dropna(subset=['age'], how='any', axis=0)
print(len(rdf))
print('\n')

# 'embarked'의 결측치 제일 빈도수 많은 값으로 대체
most_freq = rdf['embarked'].value_counts(dropna=True).idxmax()
print(most_freq)
print('\n')

# 위에랑 다른방식
# print(rdf['embarked'].describe(include='all'))
# print('\n')

rdf['embarked'].fillna(most_freq, inplace=True)

'''
STEP3 속성선택
'''

ndf = rdf[['survived', 'pclass', 'sex', 'age', 'sibsp', 'parch', 'embarked']]

# one-hot-encoding

onehot_sex = pd.get_dummies(ndf['sex'])
ndf = pd.concat([ndf, onehot_sex], axis=1)

onehot_embarked = pd.get_dummies(ndf['embarked'], prefix='town')
ndf = pd.concat([ndf, onehot_embarked], axis=1)

ndf.drop(['sex', 'embarked'], axis=1, inplace=True)

'''
STEP4 훈련/검증 데이터 분할
'''

# 속성 선택
X = ndf[['pclass', 'age', 'sibsp', 'parch', 'female', 'male', 'town_C', 'town_Q', 'town_S']]

y = ndf['survived']

from sklearn import preprocessing

X = preprocessing.StandardScaler().fit(X).transform(X)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=10)

print('train data 개수 : ', X_train.shape)
print('test data 개수 : ', X_test.shape)

'''
STEP5 SVM 분류 모형 
'''

from sklearn import svm

svm_model = svm.SVC(kernel='rbf')

svm_model.fit(X_train, y_train)

y_hat = svm_model.predict(X_test)

print(y_hat[:10])
print(y_test.values[:10])


from sklearn import metrics
svm_matrix = metrics.confusion_matrix(y_test, y_hat)
print(svm_matrix)
print('\n')


svm_report = metrics.classification_report(y_test, y_hat)
print(svm_report) 


