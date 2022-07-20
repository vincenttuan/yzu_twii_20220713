import pandas as pd
import matplotlib.pyplot as plt

起始資金 = 30
每月薪資 = 3
每月開銷 = 1
每月房租 = 1
退休年齡 = 65
預測時段 = range(25, 100, 1)
每年淨額 = pd.Series(0, index=預測時段)
每年淨額.iloc[0] = 起始資金
每年淨額.loc[:退休年齡] += 每月薪資 * 12
每年淨額 -= (每月開銷 + 每月房租) * 12
沒有投資下的總資產 = 每年淨額.cumsum()
沒有投資下的總資產.plot()

# 有投資的情況下
# 將前一年的資金的 70% 拿來投資 30% 存在銀行
投資比例 = 0.7
投資年利率 = 1.05

# arr=每年淨額, ratio=投資比例, return_rate=投資年利率
def calc(arr, ratio, return_rate):
    ret = [arr.iloc[0]]
    for v in arr[1:]:
        ret.append(ret[-1] * ratio * return_rate + ret[-1] * (1-ratio) + v)
    print(ret)
    return pd.Series(ret, 預測時段)

有投資下的總資產 = calc(每年淨額, 投資比例, 投資年利率)
有投資下的總資產.plot()

plt.grid(True)
plt.show()
