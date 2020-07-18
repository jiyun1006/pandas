import seaborn as sns

df = sns.load_dataset('titanic')

missing_df = df.isnull()
print(missing_df)
for col in missing_df.columns:
    missing_count = missing_df[col].value_counts()

    # NaN값이 존재하면 개수
    try:
        print(col, ': ', missing_count[True])
    # NaN값이 존재하지 않으면 0
    except:
        print(col, ': ', 0)

# 누락 데이터 제거

df_thresh = df.dropna(axis=1, thresh=500)
print(df_thresh.columns)

# age열에 데이터가 NaN인 경우의 모든 행 삭제
# how='any'는 하나라도 NaN면 삭제 how='all'은 모든 데이터가 NaN일시 삭제
df_age = df.dropna(subset=['age'], how='any', axis=0)
print(len(df_age))
print(df_age)
