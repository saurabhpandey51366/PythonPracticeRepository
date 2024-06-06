n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))
dictt = {}
for i in range(len(lst)):
    dictt[lst[i]] = lst[:i+1].count(lst[i])
summ = 0
for i,j in dictt.items():
    summ = summ + j - 1
print(summ)