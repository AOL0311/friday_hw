# 從鍵盤讀取一個由整數組成之序對 (a, b, c)，判斷此 3 個數值可否構成三角形。
# 若不行，則輸出 無法形成三角形; 若可以，則判斷是下列何種三角形:
# (1) 正三角形; (2) 等腰三角形; (3) 直角三角形; (4)普通三角形。

def side_detect(x, y, z):
    if x + y < z or x + z < y or y + z < x:
        return '無法形成三角形'
    else:
        if x == b == c:
            return '正三角形'
        elif x == y or x == z or y == z:
            return '等腰三角形'
        elif x ** 2 + y ** 2 == z ** 2 or x ** 2 + z ** 2 == y ** 2 or y ** 2 + z ** 2 == x ** 2:
            return '直角三角形'
        else:
            return '普通三角形'

a, b, c = map(int, input('輸入一個由整數組成之序對 a, b, c: ').split(','))

print(side_detect(a, b, c))