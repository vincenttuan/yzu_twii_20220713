# Serial 與 DataFrame
import pandas as pd
idx = pd.date_range('20220701', periods=5)
# print(idx)
s1 = pd.Series([1, 2, 3, 4, 5], index=idx)
s2 = pd.Series([7, 3, 5, 1, 9], index=idx)
s3 = pd.Series([6, 10, 2, 4, 6], index=idx)
dict = {'s1': s1, 's2': s2, 's3': s3}
df = pd.DataFrame(dict)
print(df)
# 刪除
# a = df.drop('s1', axis=1)
# a = df.drop(columns=['s1'])  # 可以省略 axis=1
# print(a)
#b = df.drop('20220701') # 預設 axis=0
#b = df.drop('20220701', axis=0)
#b = df.drop(pd.Timestamp('2022-07-01'))
#print(b)

del df['s1']  # 直接刪除 df 資料
print(df)
