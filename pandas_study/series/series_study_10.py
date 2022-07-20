import pandas as pd
# 總和練習 1
# 請求出 s.rolling(2).sum().cumsum() + 1 的最大值
s = pd.Series([4, 7, -5, 3])
print(s)
print(s.rolling(2).sum())
print(s.rolling(2).sum().cumsum())
print(s.rolling(2).sum().cumsum() + 1)


