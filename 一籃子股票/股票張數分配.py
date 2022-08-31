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

    while True:
        # 平均每一檔股票可以有多少錢買進?
        invest_money = (money / len(stock_list))
        print('每一檔股票可以買入的金額:', invest_money)
        # np.floor 往下取整數 1.2 -> 1, -1.2 -> -2
        ret = np.floor(invest_money / stock_list / 1000)
        print(ret)
        if (ret == 0).any(): # 假設 ret 列表中有 0.0 的情況
            # 若沒有匹配到張數的就踢除掉價格最大的標的
            print("剔除標的:", str(stock_list.idxmax()), "價格:", str(stock_list.max()))
            stock_list = stock_list[stock_list != stock_list.max()]
            # print(stock_list)
        else:
            break;

    # 總投資金額
    sum = (stock_list * ret * 1000).sum()
    return ret, sum, price

if __name__ == '__main__':
    # 選擇一個有交易的日期當作買入日期
    tday = datetime.date(2022, 7, 1)
    # 建議投資標的
    cond, index, roi = basket(tday)
    print('cond:', cond)
    # 投資金額
    money = 4000000
    # 建議投資分配
    ret, sum, price = portfolio(cond, money)
    print('----------------------')
    print('買進標的的張數:', ret)
    print('買進標的價格:', price.iloc[0][ret.index])
    print('預估投資金額:', money)
    print('預估買進股票檔數:', len(cond))
    print('實際投資金額:', sum)
    print('實際買進股票檔數:', len(ret))

    if (len(ret) == len(cond)):
        print('報酬率: %.2f%%' % (roi * 100))
    else:
        print('報酬率: 無(不足 %d 檔)' % (len(cond)))

