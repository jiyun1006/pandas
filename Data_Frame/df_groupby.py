import pandas as pd
import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'sex', 'class', 'fare', 'survived']]
print("승객수", len(df))
print(df.head())
print('\n')

grouped = df.groupby(['class'])
print(grouped)

for key, group in grouped:
    print('* key :', key)
    print('* number : ', len(group))
    print(group.head())
    print('\n')

average = grouped.mean()
print(average)
print('\n')

# 특정 그룹 선택
group3 = grouped.get_group('Third')
print(group3.head())
print('\n')

# 다수의 열을  group화
grouped_two = df.groupby(['class', 'sex'])

for key, group in grouped_two:
    print('* key :', key)
    print('* number :', len(group))
    print(group.head())
    print('\n')

average_two = grouped_two.mean()
print(average_two)
print('\n')
print(type(average_two))
print('\n')

group3f = grouped_two.get_group(('Third', 'female'))
print(group3f.head())