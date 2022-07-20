import pandas as pd
# Series 計算 4
s = pd.Series([100, 45, 90, 55, 78])
print(s)
s = s >= 60
print(s)
# 改變型態
s = s.astype(int)
print(s)
