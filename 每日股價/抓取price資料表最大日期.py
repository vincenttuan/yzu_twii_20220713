import sqlite3
from datetime import datetime, date, timedelta

conn = sqlite3.connect('../資料庫/財經資料庫.db')
cursor = conn.cursor()

sql = 'select max(交易日) from price'
cursor.execute(sql)
row = cursor.fetchone();
max_date = datetime.strptime(row[0], '%Y-%m-%d').date()
print('報價資料表最大日期:', max_date)
max_date_add_one_day = max_date + timedelta(days=1)
print('報價資料表開始抓取日期:', max_date_add_one_day)
