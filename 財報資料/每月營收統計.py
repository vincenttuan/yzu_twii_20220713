# 關鍵字查詢: 公開資訊觀測站
# https://mops.twse.com.tw/mops/web/index
# 彙總報表 > 營用概況 > 每月營收 > 採用IFRSs後每月營業收入彙總表
# IFRS 國際會計準則
# 範例路徑: https://mops.twse.com.tw/nas/t21/sii/t21sc03_110_10_0.html
import requests
import pandas as pd
import sqlite3
from io import StringIO

def get_monthly_report(year, month):
    # 取得上市公司xxx年xx月份(累計與當月)營業收入統計表路徑
    url = 'https://mops.twse.com.tw/nas/t21/sii/t21sc03_%d_%d_0.html' % (year-1911, month)
    # 抓取網頁
    r = requests.get(url)
    print(r.text)
    pass

if __name__ == '__main__':
    get_monthly_report(2021, 10)
