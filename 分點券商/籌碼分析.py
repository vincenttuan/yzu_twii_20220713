import time
import pandas as pd
import requests.packages.urllib3
import re
from io import StringIO

requests.packages.urllib3.disable_warnings()
headers = {'User-Agent': 'chrome'}

# 取得驗證碼
def get_code(rs):
    pass

# 傳送表單資料
def send_data(rs, stock_id, viewstate, eventvalidation):
    pass

# 解析資料
def parse_data(text):
    pass

# 主程式
if __name__ == '__main__':
    symbol = '1101'  # 股票代號



