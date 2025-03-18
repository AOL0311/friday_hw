# 從鍵盤讀取一個由整數組成之序對 (a, b, c)，判斷此 3 個數值可否構成三角形。
# 若不行，則輸出 無法形成三角形; 若可以，則判斷是下列何種三角形:
# (1) 正三角形; (2) 等腰三角形; (3) 直角三角形; (4)普通三角形。

a, b, c = map(int, input('輸入一個由整數組成之序對 a, b, c: ').split(','))

if a + b < c and a + c < b and b + c < a:
    print('無法形成三角形')
else:
    if a == b == c:
        print('正三角形')
    elif a == b or a == c or b == c:
        print('等腰三角形')
    elif a ** 2 + b ** 2 == c ** 2 or a ** 2 + c ** 2 == b ** 2 or b ** 2 + c ** 2 == a ** 2:
        print('直角三角形')
    else:
        print('普通三角形')
