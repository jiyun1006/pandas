import matplotlib.pyplot as plt
import pandas as pd

# 한글폰트 적용법
# from matplotlib import font_manager, rc
#
# font_path = "./malgun.ttf"
# font_name = font_manager.FontProperties(fname=font_path).get_name()
# rc('font', family=font_name)

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



# 스타일 서식 지정
plt.style.use('ggplot')


# 전체 plot창 사이즈
plt.figure(figsize=(14, 5))

# x축 글씨 회전
plt.xticks(rotation='vertical')

# x축, y축 데이터를 plot 함수에 입력
plt.plot(sr_one, marker='o', markersize=10)

plt.title('seoul ->  move into gunggi', size=30)
plt.xlabel('year', size=20)
plt.ylabel('counts of people', size=20)
plt.legend(labels=['seoul -> gunggi'], loc='best', fontsize=15)

plt.ylim(50000, 800000)

# 주석 다는 형식
plt.annotate('', xy=(20, 620000), xytext=(2, 290000), xycoords='data', arrowprops=dict(arrowstyle='->', lw=5))
plt.annotate('', xy=(47, 450000), xytext=(30, 580000), xycoords='data',
             arrowprops=dict(arrowstyle='->', color='olive', lw=5))
plt.annotate('increase(1970-1995)', xy=(10, 400000), rotation=25, va='baseline', ha='center', fontsize=15, )
plt.annotate('decrease(1995-2017)', xy=(40, 500000), rotation=-11, va='baseline', ha='center', fontsize=15, )

plt.show()


