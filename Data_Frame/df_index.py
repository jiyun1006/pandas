import pandas as pd
import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'sex', 'class', 'fare', 'survived']]

grouped = df.groupby(['class', 'sex'])

gdf = grouped.mean()
print(gdf)
print('\n')
print(type(gdf))
print('\n')
print(gdf.loc[('First','female')])