import pandas as pd

df1 = pd.DataFrame({'a': ['a0', 'a1', 'a2', 'a3'],
                    'b': ['b0', 'b1', 'b2', 'b3'],
                    'c': ['c0', 'c1', 'c2', 'c3']},
                   index=[0, 1, 2, 3])

df2 = pd.DataFrame({'a': ['a2', 'a3', 'a4', 'a5'],
                    'b': ['b2', 'b3', 'b4', 'b5'],
                    'c': ['c2', 'c3', 'c4', 'c5'],
                    'd': ['d2', 'd3', 'd4', 'd5']},
                   index=[2, 3, 4, 5])
print(df1, '\n')
print(df2, '\n')

# result1 = pd.concat([df1, df2])
# ignore_index는 기존의 인덱스 무시하고, 새로운 인덱스 부여
# 행방향 concat
result1 = pd.concat([df1, df2], ignore_index=True)

print(result1, '\n')

# 열방향 concat
# 기본적으로 join가 outer이므로 inner로 바꾸면 공통된 인덱스만 출력한다.
result3 = pd.concat([df1, df2], axis=1, join='inner')
print(result3, '\n')
