import pandas as pd

df = pd.read_csv('stock-data.csv')

df['new_Date'] = pd.to_datetime(df['Date'])
df.set_index('new_Date', inplace=True)

df_y = df['2018']
print(df_y)
print('\n')
df_ym = df['2018-07']
print(df_ym)
print('\n')
df_ym_cols = df.loc['2018-07', 'Start': 'High']
print(df_ym_cols)
print('\n')
df_ymd = df['2018-07-02']
print(df_ymd)
print('\n')
df_ymd_range = df['2018-06-25': '2018-06-20']
print(df_ymd_range)

# 활용

today = pd.to_datetime('2018-12-25')
df['time_delta'] = today - df.index
df.set_index('time_delta', inplace=True)

df_180 = df['180days': '189days']
print(df_180)
