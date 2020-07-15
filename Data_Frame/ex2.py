import pandas as pd

df = pd.DataFrame([[15, '남', '덕영중'], [17, '여', '수리중']])

df.index = ['학생1', '학생2']
df.columns = ['연령', '남녀', '소속']
print(df, '\n')

df.rename(columns={'연령': '나이', '남녀': '성별', '학교': '소속'}, inplace=True)
df.rename(index={'학생1': '준서', '학생2': '예은'}, inplace=True)


print(df)
