import requests
import pandas as pd
import io
import sqlite3

# 抓取每日股價並存入資料庫中
def create_record(date):
    url = 'https://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date=%s&type=ALLBUT0999&_=1659530272690' % date
    r = requests.get(url)
    lines = r.text.split("\n")
    # for line in lines:
    #     print(len(line.split('",')), line)
    newlines = []
    for line in lines:
        if len(line.split('",')) == 17:
            newlines.append(line.replace('=', ''))  # 去除有 "=" 的內容
    # 將 newlines 裡面的每一筆資料透過 \n 來串接
    # [1, 2, 3], [4, 5, 6] => "1, 2, 3\n4, 5, 6"
    data = "\n".join(newlines)
    df = pd.read_csv(io.StringIO(data)) # 將字串data轉成csv檔案格式並給pd來讀取
    print(df)

if __name__ == '__main__':
    today = '2022-08-10'
    create_record(today)
