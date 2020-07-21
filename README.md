# pandas   
*****   
>### Regression

- [STEP1] 데이터를 불러온다.   

- [STEP2] 데이터를 탐색한다.   
#### 데이터의 자료형과 개수를 확인하고, 주요 통계 정보도 확인한다.   

#### 데이터의 결측값을 제거한다.(실수형 으로 변환하기 전 결측값 제거)   

**[예시]**   
```
df['horsepower'].replace('?', np.nan, inplace=True)
df.dropna(subset=['horsepower'], axis=0, inplace=True)
df['horsepower'] = df['horsepower'].astype('float')
```   

- [STEP3] 속성 선택   
#### 분석에 사용할 열을 선택한다.   

#### 선택한 열들의 선형관계를 파악한다.   

#### 여러 plot 유형 중 알맞은 것을 사용한다.
```
# 변수들간의 모든 관계
grid_ndf = sns.pairplot(ndf)
plt.show()
plt.close()
```   

