import pandas as pd
# Series 計算 3
s = pd.Series([1, 2, -3, -4, 5], index=pd.date_range('20220701', periods=5, freq='M'))
print(s)
# 移動窗格 rolling(n)
a = s.rolling(2).sum()
print(a)
b = s.rolling(2).sum().max()
print(b)
