import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'fare']]
print(df.head())
print('\n')


def add_10(n):
    return n + 10


# 전체에 적용하려면 applymap

df_map = df.applymap(add_10)
print(df_map.head())


def missing_value(series):
    return series.isnull()


# 각 열을 인자로 전달하면서 함수 매핑
result = df.apply(missing_value, axis=0)
print(result.head())
print('\n')
print(type(result))


def min_max(x):
    return x.max() - x.min()


result = df.apply(min_max)
print(result)
print('\n')
print(type(result))
