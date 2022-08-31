import time
import pandas as pd
import requests.packages.urllib3
import re
from io import StringIO

requests.packages.urllib3.disable_warnings()
headers = {'User-Agent': 'chrome'}

# 取得驗證碼
def get_code(rs):
    res = rs.get('https://bsr.twse.com.tw/bshtm/bsMenu.aspx',
                 verify=False, stream=True, headers=headers, timeout=None)
    # print(res.text)
    # 透過 re (正則表示式來抓取 __VIEWSTATE, __EVENTVALIDATEION)
    # \s 各種空白符號, 包含換行 \n
    # \w 任意文字字元, 包含數字
    viewstate = re.search('__VIEWSTATE"\s+value=.*=', res.text)
    viewstate = viewstate.group(0)[20:]
    eventvalidation = re.search('__EVENTVALIDATION"\s+value=.*\w', res.text)
    eventvalidation = eventvalidation.group(0)[26:]
    return viewstate, eventvalidation

# 傳送表單資料
def send_data(rs, stock_id, viewstate, eventvalidation):
    pass

# 解析資料
def parse_data(text):
    pass

# 主程式
if __name__ == '__main__':
    symbol = '1101'  # 股票代號
    # 顯示所有列
    pd.set_option('display.max_rows', None)
    # 建立 session
    rs = requests.session()
    viewstate, eventvalidation = get_code(rs)
    print('viewstate', viewstate)
    print('eventvalidation', eventvalidation)


