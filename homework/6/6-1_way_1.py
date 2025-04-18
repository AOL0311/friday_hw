n = int(input('輸入要計算 n! 的 n 的值: '))

def calc(x):
    if x <= 1:
        return 1
    else:
        return x * calc(x - 1)
    
print(calc(n))
