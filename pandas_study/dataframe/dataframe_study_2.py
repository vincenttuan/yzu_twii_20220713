# Serial 與 DataFrame
import pandas as pd
import matplotlib.pyplot as plt
idx = pd.date_range('20220701', periods=5)
# print(idx)
s1 = pd.Series([1, 2, 3, 4, 5], index=idx)
s2 = pd.Series([7, 3, 5, 1, 9], index=idx)
s3 = pd.Series([6, 10, 2, 4, 6], index=idx)
dict = {'s1': s1, 's2': s2, 's3': s3}
df = pd.DataFrame(dict)
print(df)
# print(df.loc['20220703'])
# 資料形狀
print('形狀:', df.shape)
print('列數:', df.shape[0])
print('欄數:', df.shape[1])
# 繪圖
df.plot()
plt.show()
