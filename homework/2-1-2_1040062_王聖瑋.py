def calc(x, y):
    return y / ((x / 100) ** 2)

height = float(input('輸入身高(cm): '))
weight = float(input('輸入體重(kg): '))

print(f'BMI: {calc(height, weight):.2f}')