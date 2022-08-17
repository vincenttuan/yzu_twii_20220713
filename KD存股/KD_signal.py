import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    symbol = '0050'
    days = '1000'
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
        WHERE 證券代號 = '%s' 
        ORDER BY 交易日 DESC
        LIMIT %s
    ''' % (symbol, days)
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
    # print(tx)
    print('--------------------------------------------------------------')
    # 計算 K 值
    # K 是 RSV 和前一日 K 值的加權平均
    # K = (2/3) * K + (1/3) * rsv
    K = 0
    def KValue(rsv):
        global K
        K = (2/3) * K + (1/3) * rsv
        return K
    tx['K'] = 0
    tx['K'] = tx['RSV'].apply(KValue)

    # 計算 D 值
    # D 是 K值 和前一日 D 值的加權平均
    # D = (2/3) * D + (1/3) * k
    D = 0
    def DValue(k):
        global D
        D = (2/3) * D + (1/3) * k
        return D
    tx['D'] = tx['K'].apply(DValue)
    # print(tx)

    # 買賣訊號
    # 如果行情是一個明顯的漲勢，會帶動K線與D線向上升。如漲勢開始遲緩，則會反應到K值與D值，使得K值跌破D值，此時中短期跌勢確立。
    # 當K值大於D值，顯示目前是向上漲升的趨勢，因此在圖形上K線向上突破D線時，即為買進訊號。
    # 當D值大於K值，顯示目前是向下跌落，因此在圖形上K線向下跌破D線，此即為賣出訊號。
    # 上述K線與D線的交叉，須在80以上，20以下(一說70、30；視市場投機程度而彈性擴大範圍)，訊號才正確。
    # 當K值大於80，D值大於70時，表示當日收盤價處於偏高之價格區域，即為超買狀態；
    # 當K值小於20，D值小於30時，表示當日收盤價處於偏低之價格區域，即為超賣狀態。
    # 當D值跌至15以下時，意味市場為嚴重之超賣，其為買入訊號；
    # 當D值超過85以上時，意味市場為嚴重之超買，其為賣出訊號。
    # 價格創新高或新低，而KD未有此現象，此為背離現象，亦即為可能反轉的重要前兆。
    # --------------------------------------------------------------
    # 黃金交叉的買進訊號 | 死亡交叉的賣出訊號
    # 黃金交叉的買進訊號: 今天 k > d (K線向上突破D線) 昨天 k < d
    # 死亡交叉的賣出訊號: 今天 k < d (K線向下貫穿D線) 昨天 k > d
    # 判斷市場行情一般來說都是使用 D 值的數據
    # D > 80: 超買區
    # D < 15, D < 20 或 D < 30 : 超賣區
    # D = 50: 多空平衡
    # D > 50 : 多頭佔上風
    # D < 50 : 空頭佔上風
    # 製作訊號
    k = tx['K']  # k 是一個 Series
    d = tx['D']  # d 是一個 Series
    close = tx['收盤價']  # close 是一個 Series
    # Series 運算
    buy = (k > d) & (k.shift() < d.shift()) & (k < 20) & (d < 30)
    sell = (k < d) & (k.shift() > d.shift()) & (k > 90) & (d > 90)
    # print(buy)
    filter1 = (buy == True)  # 過濾出資料是 True
    filter2 = (sell == True)  # 過濾出資料是 True
    print(buy[filter1])
    print(sell[filter2])
    # 繪圖
    # 因為 buy, sell 是 bool 所以要繪圖之前請先轉成 int
    buy = buy.astype(int)  # True -> 1, False -> 0
    sell = sell.astype(int)  # True -> 1, False -> 0
    close.plot(label='close', color='gray')  # 繪製 close 線
    plt.legend()  # 圖例
    buy.plot(secondary_y=True, label='BUY', color='red')
    sell.plot(secondary_y=True, label='SELL', color='green')
    plt.legend()  # 圖例
    # close.plot(secondary_y=True, label='close', color='gray')  # 繪製 close 線
    # plt.legend()  # 圖例

    plt.title(symbol + ' KD index ' + days + ' days')  # 圖標題
    plt.grid()  # 格線
    plt.show()

