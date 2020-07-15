import matplotlib.pyplot as plt
import pandas as pd

# 하나의 그래프 표시

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

# 화면 분할2

fig = plt.figure(figsize=(20, 5))
ax = fig.add_subplot(1, 1, 1)

ax.plot(sr_one, marker='o', markerfacecolor='orange', markersize=10, color='olive', lw=2, label='seoul -> gunggi')
ax.legend(loc='best')

ax.set_ylim(50000, 800000)

ax.set_title('seoul -> gunggi', size=20)

ax.set_xlabel('year', size=12)
ax.set_ylabel('cnt people', size=12)

ax.set_xticklabels(sr_one.index, rotation=75)

# 축 눈금 라벨 크기
ax.tick_params(axis='x', labelsize=10)
ax.tick_params(axis='y', labelsize=10)

plt.show()
