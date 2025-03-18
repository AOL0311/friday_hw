n = int(input('輸入一個數: '))

def calc(x):
    if x <= 1:
        return 1
    else:
        return x * calc(x - 1)
    
print(calc(n))