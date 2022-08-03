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
print(df)


