import pandas as pd

# dates = ['2019-01-01', '2020-03-01', '2021-06-01']
#
# ts_dates = pd.to_datetime(dates)
# print(ts_dates)
#
# pr_day = ts_dates.to_period(freq='D')
# print(pr_day)
# pr_month = ts_dates.to_period(freq='M')
# print(pr_month)
# pr_year = ts_dates.to_period(freq='A')
# print(pr_year)


ts_ms = pd.date_range(start='2019-01-01', end=None, periods=6, freq='MS', tz='Asia/Seoul')
print(ts_ms)

ts_me = pd.date_range('2019-01-01', periods=6, freq='M', tz='Asia/Seoul')
print(ts_me)

ts_3m = pd.date_range('2019-01-01', periods=6, freq='3M', tz='Asia/Seoul')
print(ts_3m)

