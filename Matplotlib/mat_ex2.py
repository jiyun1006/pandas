import matplotlib.pyplot as plt
import pandas as pd

# 서브플롯 1

df = pd.read_excel('시도별 전출입 인구수.xlsx', header=0)
print(df.head())
df = df.fillna(method='ffill')

# 서울에서 전출되는 인원이 어디로 전입되는지 만드는 데이터 조정

mask = (df['전출지별'] == '서울특별시') & (df['전입지별'] != '서울특별시')
df_seoul = df[mask]
df_seoul = df_seoul.drop(['전출지별'], axis=1)
df_seoul.rename({'전입지별': '전입지'}, axis=1, inplace=True)
df_seoul.set_index('전입지', inplace=True)
# print(df_seoul.head())
sr_one = df_seoul.loc['경기도']
plt.style.use('ggplot')

# 화면 분할1
# 각각 화면의 크기 조정
fig = plt.figure(figsize=(10, 10))
# fig의 2행 1열중 1행
ax1 = fig.add_subplot(2, 1, 1)

# fig의 2행 1열중 2행
ax2 = fig.add_subplot(2, 1, 2)

ax1.plot(sr_one, 'o', markersize=10)
ax2.plot(sr_one, marker='o', markerfacecolor='green', markersize=10, color='olive', lw=2,
         label='seoul -> gunggi')
ax2.legend(loc='best')

ax1.set_ylim(50000, 800000)
ax2.set_ylim(50000, 800000)

ax1.set_xticklabels(sr_one.index, rotation=75)
ax2.set_xticklabels(sr_one.index, rotation=75)

plt.show()
