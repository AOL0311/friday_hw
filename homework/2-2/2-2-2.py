def calc(x, y, z):
    return x * 0.20 + y * 0.40 + z * 0.40

regular = int(input('請輸入平時成績: '))
mid_term = int(input('請輸入期中考成績: '))
final = int(input('請輸入期末考成績: '))

print(f'學期總成績為: {calc(regular, mid_term, final):.2f}')