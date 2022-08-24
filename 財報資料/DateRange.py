import datetime
from datetime import date

import pandas as pd

from 財報資料.抓取monthly_report資料表最大日期 import get_begin_month

start_date = date(2020, 1, 1)
#start_date = get_begin_month()
end_date = datetime.date.today()
print(start_date, type(start_date))
print(end_date, type(end_date))
daterange = pd.date_range(start_date, end_date, freq='M')
for date in daterange:
    print(date.year, date.month)
