import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('./남북한발전전력량.xlsx')

df_ns = df.iloc[[0, 5], 3:]  # 데이터를 보고 남한 북한 전력량 부분만 뽑기
df_ns.index = ['South', 'North']  # 새로운 인덱스
df_ns.columns = df_ns.columns.map(int)  # map(int)로 integer로 바꾼다.
print(df_ns.head())
print('\n')

# plt.plot(df_ns)
# plt.show()
tdf_ns = df_ns.T
print(tdf_ns)

# 선 그래프
# plt.plot(tdf_ns['South'], tdf_ns.index, label="South")
# plt.plot(tdf_ns['North'], tdf_ns.index, label="North")

# 막대 그래프
# plt.bar(tdf_ns.index, tdf_ns['South'], label="South")
# plt.bar(tdf_ns.index, tdf_ns['North'], label="North")

# 히스토그램

print(tdf_ns['South'])

plt.hist(tdf_ns['South'], 10, label="South")
plt.hist(tdf_ns['North'], 1, label="North")
plt.ylim([0,30])

plt.legend(loc="upper right")
plt.show()
