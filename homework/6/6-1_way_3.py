def factorial(x):
    result = 1

    while x > 0:
        result *= x
        x -= 1

    return result

n = int(input('輸入要計算 n! 的 n 的值: '))

print(factorial(n))