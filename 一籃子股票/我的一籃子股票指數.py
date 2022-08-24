# 透過當月營收與股價淨值比來找一籃子股票
# 我的一籃子股票指數
# 股價淨值比(pb): 5 < pb < 6
# 近三個月的營收 > 近一年的營收
# 回測驗證績效
# 計算 ROI 報酬率
import datetime
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # 選擇一個有交易的日期當作買入日期
    tday = datetime.date(2022, 7, 1)
    conn = sqlite3.connect('../資料庫/財經資料庫.db')
    # 股價 >= 2022, 7, 1
    sql = '''
        select 證券代號 as stock_id, 交易日 as date, 收盤價 from price
        where date >= '%s'
    ''' % (tday)
    # print(sql)
    price = pd.read_sql(sql, conn, parse_dates=['date'])\
              .pivot(index='date', columns='stock_id')['收盤價']
    # print(price)
    # PB 股價淨值比 = 2022, 7, 1
    sql = '''
        select symbol as stock_id, ts as date, pb 
        from BWIBBU
        where date == '%s'
    ''' % (tday)
    # print(sql)
    pb = pd.read_sql(sql, conn, parse_dates=['date'])\
           .pivot(index='date', columns='stock_id')['pb']
    # print(pb)
    # 當月營收 < 2022, 7, 1
    sql = '''
        select cast(stock_id as varchar(50)) as stock_id, date, 當月營收
        from monthly_report
        where date < '%s'
    ''' % (tday)
    # print(sql)
    rev = pd.read_sql(sql, conn, parse_dates=['date'])\
            .pivot(index='date', columns='stock_id')['當月營收']
    # print(rev)

    # 策略條件 1
    # 股價淨值比(pb): 5 < pb < 6
    condition1 = pb.columns[(pb.iloc[0] > 5) & (pb.iloc[0] < 6)]
    print('印出符合 策略條件 1 的股票:', condition1)

    # 策略條件 2
    # 近三個月的平均營收 > 近一年的平均營收
    condition2 = rev.columns[rev.iloc[-3:].mean() > rev.iloc[-12:].mean()]
    print('印出符合 策略條件 2 的股票:', condition2)

    # 策略條件 1 & 策略條件 2
    cond = condition1.intersection(condition2)
    print('策略條件 1 & 策略條件 2:', cond)

    # 編指數
    index = price[cond].mean(axis=1)
    print(index)

    # ROI
    diff = index.iloc[-1] - index.iloc[0]
    roi = diff / index.iloc[0]
    print('diff:', diff, 'roi:', roi)
    print('建議買進:', cond)
    print('回測報酬率: %.2f%%' % (roi*100))

    # 繪圖
    index.plot()
    plt.show()