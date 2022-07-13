# lambda 與 dict 字典數組應用
computer = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y
}

if __name__ == '__main__':
    # 透過 computer 操作 20, 10 相加
    result = computer.get('+')(20, 10)
    print(result)
    # 透過 computer 操作 20, 10 求餘數
    result = computer.get('%', lambda x, y: None)(20, 10)
    print(result)