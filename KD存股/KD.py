import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # 顯示所有欄位
    pd.set_option('display.max_columns', None)
    # 顯示所有列
    # pd.set_option('display.max_rows', None)
    # 設定列表寬度
    pd.set_option('display.width', 500)
    # 資料庫路徑
    db_path = '../資料庫/財經資料庫.db'
    # 資料庫連線
    conn = sqlite3.connect(db_path)
    # 抓取最近 500 天的交易資料
    sql = '''
        SELECT 交易日 AS date, 開盤價, 最高價, 最低價, 收盤價 
        FROM price 
        WHERE 證券代號 = '0050' 
        ORDER BY 交易日 DESC
        LIMIT 1000
    '''
    # print(sql)
    # 將資料讀入 pandas DataFrame
    tx = pd.read_sql(sql, conn)
    # 建立 index
    tx.index.name = 'date'
    # 資料排序
    tx = tx.sort_index(ascending=False)
    # 將 index 轉為日期格式
    tx.index = pd.DatetimeIndex(tx['date'])
    # print(tx)
    print('--------------------------------------------------------------')
    # RSV
    # RSV = (今日收盤價 - 最近9日的最低價) / (最近9日的最高價 - 最近9日的最低價) * 100
    # 計算最近9日的最高價
    tx['9dMax'] = tx['最高價'].rolling(9).max()
    # 計算最近9日的最低價
    tx['9dMin'] = tx['最低價'].rolling(9).min()
    # 刪除 NaN
    tx = tx.dropna()
    # 計算 RSV
    tx['RSV'] = 0
    tx['RSV'] = 100 * (tx['收盤價'] - tx['9dMin']) / (tx['9dMax'] - tx['9dMin'])
    print(tx)
    print('--------------------------------------------------------------')