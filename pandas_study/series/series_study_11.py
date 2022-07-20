import pandas as pd

s = pd.Series([100, 50, 130, 40, 55], index=pd.date_range('20220701', periods=5))
print(s)
s = s.shift()
print(s)
# 將 NaN 轉換成 0
s = s.fillna(0)
print(s)
