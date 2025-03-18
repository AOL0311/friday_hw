n = int(input('輸入一個數: '))

ans = 1

for i in range(1, n + 1):
    ans *= i

print(ans)