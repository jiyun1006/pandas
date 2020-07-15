import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/home/jiyoon/다운로드/part/part3/auto-mpg.csv', header=None)

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year', 'origin',
              'name']

print(df.head())
print('\n')
print(df.tail())
print('\n')
print(df.shape)
print('\n')
print(df.info())
print('\n')

# 각 열의
print(df.describe())
print('\n')
print(df.describe(include='all'))
print('\n')

# 각 열의 개수
print(df.count())
print('\n')

print(type(df.count()))
print('\n')

# 각 열의 고유값 측정
unique_values = df['origin'].value_counts()
print(unique_values)
print('\n')

print(type(unique_values))

# 평균값
print(df.mean())
print('\n')
print(df['mpg'].mean())
print(df.mpg.mean())
print('\n')
print(df[['mpg', 'weight']].mean())

# 중간값

print(df.median())
print('\n')
print(df.mpg.median())

# 최대값

print(df.max())
print('\n')
print(df.mpg.max())

# 최소값

print(df.min())
print('\n')
print(df.mpg.min())

# 표준편차

print(df.std())
print('\n')
print(df.mpg.std())

# 상관계수

print(df.corr())
print('\n')
print(df[['mpg', 'weight']].corr())

# 산점도
# plt.scatter(df['weight'], df['mpg'])
# plt.show()

# 박스 플롯
plt.boxplot([df['mpg'], df['cylinders']])
plt.show()
