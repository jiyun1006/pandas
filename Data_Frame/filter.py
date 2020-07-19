import seaborn as sns

titanic = sns.load_dataset('titanic')

# 'age'의 조건을 충족하는 행만 출력
mask1 = (titanic.age >= 10) & (titanic.age < 20)
df_teenage = titanic.loc[mask1, :]
print(df_teenage.head())

# 'age'와 'sex'의 두 개의 열의 조건을 만족하는 행만 출력
mask2 = (titanic.age < 10) & (titanic.sex == 'female')
df_female_under10 = titanic.loc[mask2, :]
print(df_female_under10.head())