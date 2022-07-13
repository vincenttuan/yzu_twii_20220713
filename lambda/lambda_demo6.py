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

# 3. 過濾 filter(lambda parameter_list: expression, iterable)
# iterable 指的就是數組
nums = [50, 2, 10, 40]
# 想要過濾出 >20 的資料
result = filter(lambda x: x > 20, nums)
print(result, type(result), list(result))  # 轉 list

# 4. 轉換 map(lambda parameter_list: expression, iterable)
scores = [50, 80, 90, 30]  # [False, True, True, False]
result = map(lambda x: x >= 60, scores)
print(result, type(result), list(result))
# 動動腦
scores = [50, 80, 90, 30]  # [0, 1, 1, 0]
result = map(lambda x: 1 if x >= 60 else 0, scores)
print(result, type(result), list(result))



