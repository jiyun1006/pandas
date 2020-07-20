import pandas as pd
import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'sex', 'class', 'fare', 'survived']]

grouped = df.groupby(['class'])

std_all = grouped.std()
print(std_all)
print('\n')
print(type(std_all))
print('\n')

std_fare = grouped.fare.std()
print(std_fare)
print('\n')
print(type(std_fare))
print('\n')


def min_max(x):
    return x.max() - x.min()


# 집계연산을 그룹객체에 하려면 agg 이용
agg_minmax = grouped.agg(min_max)
print(agg_minmax.head())
print('\n')

agg_all = grouped.agg(['min', 'max'])
print(agg_all.head())
print('\n')

agg_sep = grouped.agg({'fare': ['min', 'max'], 'age': 'mean'})
print(agg_sep.head())
print('\n')


# age_mean = grouped.age.mean()
# print(age_mean)
# print('\n')
#
# age_std = grouped.age.std()
# print(age_std)
# print('\n')
#
# for key, group in grouped.age:
#     group_zscore = (group - age_mean[key]) / age_std[key]
#     print(' * origin :', key)
#     print(group_zscore.head(3))
#     print('\n')
#

# transform

def z_score(x):
    return (x - x.mean()) / x.std()


age_zscore = grouped.age.transform(z_score)
print(age_zscore.loc[[1, 9, 0]])
print('\n')
print(len(age_zscore))
print('\n')
print(age_zscore.loc[0:9])
print('\n')
print(type(age_zscore))
print('\n')


# filter

grouped_filter = grouped.filter(lambda x : len(x) >= 200)
print(grouped_filter.head())
print('\n')
print(type(grouped_filter))