import pandas as pd
'''
有一檔股票 2022-07-01~07 價格 = 10
          2022-07-08~10 價格 = 15
'''
s = pd.Series(10, index=pd.date_range('20220701', periods=10))
print(s)
s.loc['2022-07-08':] += 5
print(s)

