'''
資料類型: DataFrame
DataFrame就像是我們在使用 Excel表格一樣
是一個二維的數據(index, column)
可以透過 index, column來找到我們要的資料
'''
import pandas as pd
data = {
    'name': ['Bob', 'John', 'Mary', 'Helen', 'Jo', 'Jack', None],
    'birth': [2000, 2001, None, 2000, 2001, 2001, 2003],
    'score': [80, None, 100, 100, 90, 80, 70]
}
# print(data)
df = pd.DataFrame(data)
df = df.dropna()  # 將有 None 的資料列刪除
print(df)
print(df.loc[3])  # loc 指的是 index 欄位中的內容
print(df.iloc[3])  # loc 指的是位置 = 3


