import requests
import pandas as pd
import io

date = '20220803'
url = 'https://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date=%s&type=ALLBUT0999&_=1659530272690' % date
r = requests.get(url)
#print(r, r.text)
lines = r.text.split("\n")
newlines = []
for line in lines:
    if len(line.split('",')) == 17:
        newlines.append(line.replace('=', ''))
#print(newlines)
data = '\n'.join(newlines)
df = pd.read_csv(io.StringIO(data))
# 將全部資料變為 str
df = df.astype(str)
# 除去內容中有[,]的資料
# def func(s):
#     return s.str.replace(',', '')
# df = df.apply(func)
df = df.apply(lambda s: s.str.replace(',', ''))
# 將證券代號設定為 index
df = df.set_index('證券代號')
# 去除非數字的資料 (coerce 表示若轉換失敗就賦予 NaN)
df = df.apply(lambda s: pd.to_numeric(s, errors='coerce'))
# 將欄位有 NaN的都要移除
# axis(0:index, 1:column) 預設是 0
# how: 'any', 'all' 預設是 'any'
# 'any': 如果有存在任何 NaN, 則刪除該行或該列
# 'all': 如果所有內容 NaN, 則刪除該行或該列
df = df.dropna(axis=1, how='all')
#print(df)
# 查出今日收盤價比開盤價高出 8% 的股票
#print(df['收盤價'] / df['開盤價'] >= 1.08)
print(df[df['收盤價'] / df['開盤價'] >= 1.08])



