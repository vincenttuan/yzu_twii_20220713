# Python Lambda 語法
# 假設要定義一組 f(x) = x * x - x
def func(x):  # 一般函式
    result = x * x - x
    return result

if __name__ == '__main__':
    x = 10
    result_value = func(x)  # 調用一般函式寫法
    print('x: %d result_value: %d' % (x, result_value))
    # Lambda 運算
    # myfunc 就是一個 lambda 函式
    myfunc = lambda x: x * x - x
    result_value = myfunc(x)  # 調用lambda函式寫法
    print('x: %d result_value: %d' % (x, result_value))

