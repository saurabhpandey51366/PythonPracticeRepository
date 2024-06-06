a = [3, 4, 5, 3, 9, 10, 11, 11, 13, 14, 1]
count = 1
for i in range(1, len(a)):
    temp = -1
    for j in a[:i]:
        if a[i] <= j:
            temp = 0
            break
    if temp != 0:
        count += 1
print(count)