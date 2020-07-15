import pandas as pd

tup_data = ('영민', ' 2010-05-01', '여', True)
sr = pd.Series(tup_data, index=['이름', '생년월일', '성별', '학생여부'])

print(sr)

print('\n')
print(sr[[1, 2]])
print('\n')

print(sr[['생년월일', '성별']])

print('\n')

print(sr['생년월일':])