import sqlite3
from datetime import datetime, date, timedelta

def get_begin_day():
    # 資料庫連線
    conn = sqlite3.connect('../資料庫/財經資料庫.db')
    # 資料指標
    cursor = conn.cursor()
    sql = 'select max(交易日) from price'
    # 透過資料指標去執行 sql
    cursor.execute(sql)
    # fetchone 得到一筆資料
    row = cursor.fetchone();
    print(row, type(row))
    # row[0] 第一筆資料
    print(row[0], type(row[0]))
    # strptime 字串轉時間日期, .date() 轉日期
    max_date = datetime.strptime(row[0], '%Y-%m-%d').date()
    print('報價資料表最大日期:', max_date, type(max_date))
    # timedelta(days=1) 加一天
    max_date_add_one_day = max_date + timedelta(days=1)
    print('報價資料表開始抓取日期:', max_date_add_one_day)
    return max_date_add_one_day

if __name__ == '__main__':
    print(get_begin_day())
