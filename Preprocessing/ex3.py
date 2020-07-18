# 평균으로 누락 데이터 바꾸기
import seaborn as sns

df = sns.load_dataset('titanic')

print(df['age'].head(10))
print('\n')

mean_age = df['age'].mean(axis=0)
df['age'].fillna(mean_age, inplace=True)

print(df.head(10))

max_town = df['embark_town'].value_counts(dropna=True).idxmax()

df['embark_town'].fillna(max_town, inplace=True)
print(df['embark_town'])
