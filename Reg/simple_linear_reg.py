import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('./auto-mpg.csv', header=None)

'''
[STEP1] 데이터 불러오기
'''
df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year', 'origin',
              'name']

print(df.head())
print('\n')

pd.set_option('display.max_columns', 10)
print(df.head())
print('\n')
'''
[STEP2] 데이터 탐색(정보 확인)
'''
print(df.info())
print('\n')

print(df.describe())
print('\n')

# 데이터 타입 변경

print(df['horsepower'].unique())
print('\n')

# ?가 horsepower열에 있으므로 대체한다.
df['horsepower'].replace('?', np.nan, inplace=True)
df.dropna(subset=['horsepower'], axis=0, inplace=True)
df['horsepower'] = df['horsepower'].astype('float')

print(df.describe())
print('\n')
'''
[STEP3] 속성 선택
'''
# 분석에 사용할 열을 선택한다.

ndf = df[['mpg', 'cylinders', 'horsepower', 'weight']]
print(ndf.head())
print('\n')

# weigth와 mpg의 선형관계 확인
# plot1
# ndf.plot(kind='scatter', x='weight', y='mpg', c='coral', s=10, figsize=(10, 5))
# plt.show()
# plt.close()

# plot2
# fig = plt.figure(figsize=(10, 5))
# ax1 = fig.add_subplot(1, 2, 1)
# ax2 = fig.add_subplot(1, 2, 2)
# sns.regplot(x='weight', y='mpg', data=ndf, ax=ax1)
# sns.regplot(x='weight', y='mpg', data=ndf, ax=ax2, fit_reg=False)
# plt.show()
# plt.close()

# plot3
sns.jointplot(x='weight', y='mpg', data=ndf)
sns.jointplot(x='weight', y='mpg', kind='reg', data=ndf)
# plt.show()
# plt.close()

# plot4
# 변수들간의 모든 관계
grid_ndf = sns.pairplot(ndf)
# plt.show()
# plt.close()

'''
[STEP4] 훈련/검증 데이터 분할
'''
# 'mpg'와 선형관계를 갖는 열들을 독립변수로 선언한다.
X = ndf[['weight']]  # 독립변수 X
y = ndf['mpg']  # 종속 변수 y

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=10)

print('train data개수 : ', len(X_train))
print('test data개수 : ', len(X_test))

'''
[STEP5] 모형 학습 및 검증
'''

from sklearn.linear_model import LinearRegression

print(X_train)
lr = LinearRegression()

lr.fit(X_train, y_train)

# 결정계수 구하기
r_square = lr.score(X_test, y_test)
print(r_square)

# 회귀식 구하기
# 회귀식의 기울기
print('기울기 a: ', lr.coef_)
print('\n')

# 회귀식의 y절편
print('y절편 b', lr.intercept_)
print('\n')

# 전체 X데이터를 입력하여 예측한 값 y_hat을 실제 값과 비교

y_hat = lr.predict(X) # 예측값

plt.figure(figsize=(10, 5))
ax1 = sns.distplot(y, hist=False, label='y')
ax2 = sns.distplot(y_hat, hist=False, label='y_hat', ax=ax1)
plt.show()
plt.close()
# 결과를 보면 예측값과 실제값의 편향된 위치가 다르다. 따라서 오차를 더 줄일 필요가 있다.