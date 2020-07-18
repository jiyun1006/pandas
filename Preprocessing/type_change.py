# 자료형 변환

import pandas as pd

df = pd.read_csv('./auto-mpg.csv', header=None)

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year', 'origin',
              'name']

print(df.dtypes)
print('\n')

# 누락 데이터 중 NaN이 아닌 값이 '?'를 NaN으로 바꾸고 그 다음에 삭제한다.
# 라이브러리 numpy에서 np.nan을 이용해서 replace 한다.
import numpy as np

df['horsepower'].replace('?', np.nan, inplace=True)
df.dropna(subset=['horsepower'], axis=0, inplace=True)
df['horsepower'] = df['horsepower'].astype('float')

print(df['horsepower'].dtypes)

# 숫자 데이터가 뜻하는 나라 이름을 각각 변경해준다.
print(df['origin'].unique())
df['origin'].replace({1: 'USA', 2: 'EU', 3: 'JPN'}, inplace=True)

# 고유값이 반복적으로 나타나면 범주형이 효율적이다.
df['origin'] = df['origin'].astype('category')
print(df['origin'].dtypes)

# 문자열로 바꾸는 코드
# df['origin'] = df['origin'].astype('str')


# 연도는 숫자의 상대적인 크기가 의미가 없다. 그러므로 범주형으로 순서를 나타내는 것이 효율적이다.
print(df['model year'].sample(3))
df['model year'] = df['model year'].astype('category')
print(df['model year'].sample(3))
