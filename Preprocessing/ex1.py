import seaborn as sns

df = sns.load_dataset('titanic')

print(df.head())
print(df.info())

# 열의 NaN 개수 계산하기

nan_deck = df['deck'].value_counts(dropna=False)
print(nan_deck)
