import pandas as pd
# Series 計算 4
s = pd.Series([1, 2, 3, 4, 5], index=pd.date_range('20220701', periods=5))
print(s)
# 數學運算子直接運算
print(s + 1)
print(s - 1)
print(s * 2)
print(s / 3)
print(s > 3)
print(s < 3)



