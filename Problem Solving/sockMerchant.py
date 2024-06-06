a = [10, 20, 20, 10, 10, 30, 50, 10, 20]
key = []
value = []
for i in a:
    if i not in key:
        key.append(i)
        value.append(0)
for i in a:
    value[key.index(i)] += 1
res = 0
for i in value:
    if i > 1:
        res += int(i/2)
print(res)