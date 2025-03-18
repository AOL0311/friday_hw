lst = [[2, 4, 5], [5, 8, None], [10, 3, 4]]

for i, j in enumerate(lst):
    if None in j:
        print(f'第 {i + 1} 組: Incomplete data')
    else:
        print(f'第 {i + 1} 組: 總和為 {sum(j)}')