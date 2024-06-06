n = int(input())
temp = n
lst = []
while temp > 0:
    lst.append(temp)
    temp = temp // 2
lst.reverse()
for i in lst:
    print(i % 2, end="")