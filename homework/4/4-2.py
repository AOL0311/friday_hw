d1 = {'large':34, 'medium':28, 'small':20}

print(f'1) 建立一個由 d1 所有鍵所組成的串列。{list(d1.keys())}')
print(f'2) 建立一個由 d1 所有值所組成的序對。{tuple(d1.values())}')
print(f'3) 建立一個由 d1 所有鍵值對所組成的串列，其中鍵和值以序對表示。{list(d1.items())}')

d1.setdefault('large', 36)
print(f"4) 如果執行 d1.setdefault('large', 36)，會得到什麼結果？{d1}\n試說明原因。")
# d1 中已含有 large 及其對應值，故 setdefault 不影響結果

d1.setdefault('xlarge', 40)
print(f"5) 如果執行 d1.setdefault('xlarge', 40)，會得到什麼結果？{d1}\n試說明原因。")
# d1 中不含有 xlarge 鍵，故 setdefault 中的鍵值將直接加入結果