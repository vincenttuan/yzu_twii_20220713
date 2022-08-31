import sqlite3

from 一籃子股票.我的一籃子股票指數 import basket
import numpy as np
import pandas as pd
import datetime

# 分配張數
def portfolio(stock_list, money):
    # 取得最新股價
    conn = sqlite3.connect('../資料庫/財經資料庫.db')
    sql = '''
            select 證券代號 as stock_id, 交易日 as date, 收盤價 from price
            where date == '%s'
        ''' % (tday)
    # print(sql)
    price = pd.read_sql(sql, conn, parse_dates=['date']) \
        .pivot(index='date', columns='stock_id')['收盤價']
    print(price)
    print(stock_list)

    stock_list = price.iloc[0][stock_list]
    print(stock_list)

if __name__ == '__main__':
    # 選擇一個有交易的日期當作買入日期
    tday = datetime.date(2022, 7, 1)
    # 建議投資標的
    cond, index = basket(tday)
    print('cond:', cond)
    # 投資金額
    money = 300000
    # 建議投資分配
    portfolio(cond, money)
