def calc(x):
    if x < 1:
        return 70
    else:
        return ((((x * 1000) - 1000) // 200) * 5) + 70

kilometer = float(input('輸入里程(km): '))

print(f'{calc(kilometer):.0f}元')