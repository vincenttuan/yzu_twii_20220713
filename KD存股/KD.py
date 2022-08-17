import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # 顯示所有欄位
    pd.set_option('display.max_columns', None)
    # 顯示所有列
    pd.set_option('display.max_rows', None)
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
    print(sql)

