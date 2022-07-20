import pandas as pd

print(pd.__version__)
# Series 是一個類似陣列的物件(一維陣列)
# 建立 Series 物件可以使用 list 數組/陣列
nums = [4, 7, -5, 3]  # 預設的 index = 0, 1, 2, 3
s = pd.Series(nums)
print(s)
s = pd.Series([4, 7, -5, 3], index=['a', 'b', 'c', 'd'])
print(s)
date = pd.date_range('20220701', periods=4)
print(date)
s = pd.Series([101, 102, 103, 102], index=date)
print(s)
