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
    r.encoding = 'big5'
    # 將網頁資料透過 StringIO 給 pandas 讀取
    # 安裝 lxml 套件
    dfs = pd.read_html(StringIO(r.text))
    print(len(dfs))
    # 顯示所有欄,列
    pd.set_option('display.max.columns', None)
    pd.set_option('display.max.rows', None)
    # 設定欄寬
    pd.set_option('display.width', 5000)
    '''
    for df in dfs:
        # shape 得到表格的 (rows, columns) 資料
        # print(df.shape, df.shape[0], df.shape[1])
        if df.shape[1] == 11:
            print(df)
    '''
    # print([df for df in dfs if df.shape[1] == 11])
    df = pd.concat([df for df in dfs if df.shape[1] == 11])

    # 設定 column 名稱
    # print(df.columns.get_level_values(0))
    # print(df.columns.get_level_values(1))
    df.columns = df.columns.get_level_values(1)

    # 過濾資料
    # 將公司代號欄位中有出現'合計'或'總計'的紀錄刪除
    df = df[df['公司代號'] != '合計']
    df = df[df['公司代號'] != '總計']
    # 將當月營收數字化若當月營收不能變為數字的以 NaN 取代(errors='coerce')
    df['當月營收'] = pd.to_numeric(df['當月營收'], 'coerce')
    # 新增交易日欄位
    df['交易日'] = '%d-%d-10' % (year, month)
    # 將交易日與公司代號設定複合 index (共列 index)
    df = df.set_index(['交易日', '公司代號'])
    # 變更 index 名稱
    # '交易日', '公司代號' 改成 'date', 'stock_id'
    df.index.names = ['date', 'stock_id']
    print(df)


if __name__ == '__main__':
    get_monthly_report(2021, 10)
