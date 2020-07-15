import pandas as pd
import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'fare']]
print(df.head())
print('\n')
print(type(df))
print('\n')

add = df + 10
print(add.head())
print('\n')
print(type(add))
