import seaborn as sns
import pandas as pd

pd.set_option('display.max_columns', 10)
pd.set_option('display.max_colwidth', 20)

titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'sex', 'class', 'fare', 'survived']]
print(df.head())
print('\n')

pdf1 = pd.pivot_table(df, index='class', columns='sex', values='age', aggfunc='mean')
print(pdf1.head())

pdf2 = pd.pivot_table(df, index=['class', 'sex'], columns='survived', values=['age', 'fare'], aggfunc=['mean', 'max'])

pd.set_option('display.max_columns', 10)
print(pdf2.head())
print('\n')

print(pdf2.index)
print(pdf2.columns)
print('\n')

print(pdf2.xs(('First', 'female')))
print('\n')
print(pdf2.xs('male', level='sex'))
