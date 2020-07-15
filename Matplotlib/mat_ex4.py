import matplotlib.pyplot as plt
import pandas as pd

# 한플롯에 여러 그래프 표시

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


col_years = list(map(str, range(1970, 2018)))
df_3 = df_seoul.loc[['충청남도', '경상북도', '강원도'], col_years]

plt.style.use('ggplot')

fig = plt.figure(figsize=(20, 5))
ax = fig.add_subplot(1, 1, 1)

ax.plot(col_years, df_3.loc['충청남도', :], marker='o', markerfacecolor='green', markersize=10, color='olive', lw=2,
        label='seoul -> chungnam')
ax.plot(col_years, df_3.loc['경상북도', :], marker='o', markerfacecolor='blue', markersize=10, color='skyblue', lw=2,
        label='seoul -> kungbuk')
ax.plot(col_years, df_3.loc['강원도', :], marker='o', markerfacecolor='red', markersize=10, color='magenta', lw=2,
        label='seoul -> kangwon')

ax.legend(loc='best')

ax.set_title('seoul -> chungnam,kungbuk,kangwon', size=20)

ax.set_xlabel('year', size=12)
ax.set_ylabel('cnt people', size=12)

ax.set_xticklabels(col_years, rotation=90)

ax.tick_params(axis='x', labelsize=10)
ax.tick_params(axis='y', labelsize=10)

plt.show()
