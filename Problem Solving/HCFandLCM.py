lst = list(map(int, input().split()))
x = lst[0]
y = lst[1]
for i in range(int(min(x, y)), -1, -1):
    if x % i == 0 and y % i == 0:
        temp = i
        break
print(temp)
