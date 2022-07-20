import pandas as pd

date = pd.date_range('20220701', periods=4)
s = pd.Series([101, 102, 103, 104], index=date)
print(s)
print(s.index)
print(s.index.values)
print(s.values)
print(s.loc['20220703'])  # 根據 key 來查詢資料
print(s.iloc[1])  # 查詢維度=1內容
# 透過簡易運算式來查詢
expr = s > 102
print(s.loc[expr])
print(s.loc[s > 102])

