n = int(input('輸入一個數: '))

ans = 1

while n > 0:
    ans *= n
    n -= 1

print(ans)