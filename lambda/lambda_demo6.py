# Lambda 綜合練習
import math
# 1. lambda parameter_list: expression
max_func = lambda a, b: a if a > b else b
max_value = max_func(10, 20)
print('max_value:', max_value)

# 2. (lambda parameter_list: expression)(argument)
bmi_value = (lambda h, w: w / math.pow(h/100, 2))(170, 60)
print(bmi_value)
bmi_value = (lambda h, w: w / ((h/100)**2))(170, 60)
print(bmi_value)

# 過濾 filter(lambda parameter_list: expression, iterable)
# iterable 指的就是數組
nums = [50, 2, 10, 40]
# 想要過濾出 >20 的資料

