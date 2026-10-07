lst = [1, 2, 2, 3, 4, 4, 5]
print(list(set(lst)))                # fast, order may change
print(list(dict.fromkeys(lst)))      # keeps original order