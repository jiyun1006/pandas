import pandas as pd

exam_data = {'수학': [90, 80, 70], '영어': [98, 89, 95], '음악': [85, 95, 100], '체육': [100, 90, 90]}

df = pd.DataFrame(exam_data, index=['서준', '우현', '인아'])

print(df)
print('\n')

# 행 삭제
# df2 = df[:]
# df2.drop('우현', inplace=True)
# print(df2)
# print('\n')
#
#
# df3 = df[:]
# df3.drop(['우현', '인아'], axis=0, inplace=True)
# print(df3)


# 열 삭제
# df4 = df.copy()
# df4.drop('수학', axis=1, inplace=True)
# print(df4)
#
# df5 = df.copy()
# df5.drop(['영어', '음악'], axis=1, inplace=True)
# print(df5)


label1 = df.loc['서준':'우현']
label2 = df.loc[['서준','인아']]
position1 = df.iloc[0:2]
print(label1)
print('\n')
print(position1)
print('\n')
print(label2)