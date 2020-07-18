import pandas as pd
import numpy as np

df = pd.read_csv('./auto-mpg.csv', header = None)

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year', 'origin',
              'name']

df['horsepower'].replace('?', np.nan, inplace=True)
df.dropna(subset=['horsepower'], axis=0, inplace=True)
df['horsepower'] = df['horsepower'].astype('float')

print(df.horsepower.describe())
print('\n')

df.horsepower = df.horsepower/abs(df.horsepower.max())

print(df.horsepower.head())
print(df.horsepower.describe())