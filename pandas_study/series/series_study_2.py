import pandas as pd

date = pd.date_range('20220701', periods=4)
s = pd.Series([101, 102, 103, 104], index=date)
print(s)
print(s[1])  # 1 表示 index
print(s[0:3])  # 0 <= index < 3
print(s[:3])   # 從頭 <= index < 3
print(s[2:])   # 2 <= index 到最末端的元素

