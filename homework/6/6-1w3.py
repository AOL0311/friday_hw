n = int(input('輸入要計算 n! 的 n 的值: '))

ans = 1

while n > 0:
    ans *= n
    n -= 1

print(ans)
