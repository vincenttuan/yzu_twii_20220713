# yzu_twii_20220713
元智大學 Python 小資族股票分析課程

# 取得股價
date = '20220729'
url = 'https://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date=%s&type=ALLBUT0999&_=1637142255914' % date
r = requests.get(url)
