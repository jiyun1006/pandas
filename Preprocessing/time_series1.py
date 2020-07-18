import pandas as pd

# 문자열을 timestamp로 변환

df = pd.read_csv('stock-data.csv')

df['New_date'] = pd.to_datetime(df['Date'])

df.set_index('New_date', inplace=True)
df.drop('Date', axis=1, inplace=True)

print(df.head())
print(df.info())
