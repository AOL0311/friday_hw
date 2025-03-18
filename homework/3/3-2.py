tuple1 = (2, 4, 6, 8, 10, 12)
tuple2 = (tuple (i * 2 for i in range(1, 7)))
tuple3 = tuple(i ** 2 for i in tuple1)

print(f'1) tuple1 包含 {len(tuple1)} 個元素。')
print(f'2) tuple1 和 tuple2 是否相等？\n{tuple1 == tuple2}')
print(f'3) tuple1 的第 2 ~ 6 個元素\n {tuple1[1:6]}')
print(f'4) 元素 8 第一次出現在序對中的索引。\n索引 = {tuple1.index(8)}')
print(f'5) 從 tuple1 建立 tuple3，令它的每個元素為 tuple1 每個元素的平方。\ntuple3 = {tuple3}')