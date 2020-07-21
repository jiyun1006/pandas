# pandas   
*****   
># Regression

> [STEP1] 데이터를 불러온다.   

> [STEP2] 데이터를 탐색한다.   
> > 데이터의 자료형과 개수를 확인하고, 주요 통계 정보도 확인한다.   

> > 데이터의 결측값을 제거한다.(실수형 으로 변환하기 전 결측값 제거)   

**[예시]**   
```
df['horsepower'].replace('?', np.nan, inplace=True)
df.dropna(subset=['horsepower'], axis=0, inplace=True)
df['horsepower'] = df['horsepower'].astype('float')
```   

### [STEP3] 속성 선택   
#### 분석에 사용할 열을 선택한다.   

#### 선택한 열들의 선형관계를 파악한다.   

#### 여러 plot 유형 중 알맞은 것을 사용한다.
```
# 변수들간의 모든 관계
grid_ndf = sns.pairplot(ndf)
plt.show()
plt.close()
```  
<img src="https://user-images.githubusercontent.com/52434993/88068197-d6fcec00-cbaa-11ea-9ba1-03adca6922da.png" width="50%"></img>   

### [STEP4] 훈련/검증 데이터 분할   
#### 데이터셋을 구분한다. (훈련용 / 검증용 - 7 : 3)   

```
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=10)

```   

### [STEP5] 모형 학습 및 검증   
#### 결정계수를 구하고 회귀식을 구한다.   

#### 실제 데이터와 예측값을 비교한다.   

```
y_hat = lr.predict(X) # 예측값

plt.figure(figsize=(10, 5))
ax1 = sns.distplot(y, hist=False, label='y')
ax2 = sns.distplot(y_hat, hist=False, label='y_hat', ax=ax1)
```   

<img src="https://user-images.githubusercontent.com/52434993/88068750-9651a280-cbab-11ea-838b-fcfa48026cb2.png" width="70%"></img>   

*이 그래프에서 실제값은 왼쪽으로 편향되었고, 예측값이 오른쪽으로 편향된 모습을 본인다.*   
*따라서 모형의 오차를 더 줄일 필요가 있다.*   
*다중회귀분석으로 여러 독립변수를 통한 모델을 만든다.*


