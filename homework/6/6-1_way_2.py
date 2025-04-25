def calc(x):
    result = 1
    for i in range(1, x + 1):
        result *= i
    return result

n = int(input('輸入要計算 n! 的 n 的值: '))
print(calc(n))
