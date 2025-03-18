s1 = {1, 8, 9, 7, 6}
s2 = {2, 5, 6, 8, 9}

print(f'1) S1 包含 {len(s1)} 個元素')
print(f'2) S1 是否為 S2 的子集？ {s1.issubset(s2)}')
print(f'3) S1 和 S2 的聯集。{s1.union(s2)}')
print(f'4) S1 和 S2 的交集。{s1.intersection(s2)}')
print(f'5) S1 和 S2 的差集。{s1.difference(s2)}')
print(f'6) S1 的元素總和 = {sum(s1)}')