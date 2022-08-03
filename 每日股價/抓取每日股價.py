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
print(df)



