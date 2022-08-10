'''
https://pypi.org/project/mplfinance/
安裝 pip install --upgrade mplfinance
'''
import sqlite3
import pandas as pd
import mplfinance as mpf

if __name__ == '__main__':
    # 資料庫路徑
    db_path = '../資料庫/財經資料庫.db'
    conn = sqlite3.connect(db_path)
    # 查找某一檔股票最近n天的股價資料
    symbol = '0050'
    amount = '20'
    sql = '''
        select 交易日 as Date, 開盤價 as Open, 最高價 as 'High',
               最低價 as Low, 收盤價 as Close, 成交金額 as Volume
        from price
        where 證券代號 = '%s' order by 交易日 desc limit %s        
    ''' % (symbol, amount)
    print(sql)
    # 將資料讀進 DataFrame
    data = pd.read_sql(sql, conn)
    data = data.sort_index(ascending=False)  # 根據 index 由大到小
    data.index = pd.DatetimeIndex(data['Date'])
    print(data)

    # mpf.plot(data)
    # mpf.plot(data, type='candle')
    # mpf.plot(data, type='candle', mav=(3, 6, 9))
    # mpf.plot(data, type='candle', mav=(3, 6, 9), volume=True)
    mydpi = 135
    myfigsize = (800/mydpi, 600/mydpi)
    # mpf.plot(data, type='candle', mav=(3, 6, 9), volume=True, figsize=myfigsize)
    mpf.plot(data, type='candle', mav=(3, 6, 9), volume=True, figsize=myfigsize, savefig='chart.png')


