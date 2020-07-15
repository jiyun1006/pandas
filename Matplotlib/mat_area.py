import matplotlib.pyplot as plt
import pandas as pd

# 한글폰트 적용법
from matplotlib import font_manager, rc

font_path = "./malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

# 면적 그래프

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
df_4 = df_seoul.loc[['충청남도', '경상북도', '강원도', '전라남도'], col_years]
df_4 = df_4.T

plt.style.use('ggplot')

df_4.index = df_4.index.map(int)

# 방법1

# df_4.plot(kind='area', stacked=True, alpha=0.2, figsize=(20, 10))
#
# plt.title('seoul -> other city', size=30)
# plt.ylabel('cnt people', size=20)
# plt.xlabel('year', size=20)
# plt.legend(loc='best', fontsize=15)


# 방법2
# axes 객체로 만들면 더 세세하게 커스텀할 수 있다.

ax = df_4.plot(kind='area', stacked=True, alpha=0.2, figsize=(20, 10))
print(type(ax))
ax.set_title('서울 -> 타도시 인구 이동', size=30, color='brown', weight='bold')
ax.set_ylabel('이동 인구 수', size=20, color='blue')
ax.set_xlabel('기간', size=20, color='blue')
ax.legend(loc='best', fontsize=15)

plt.show()
