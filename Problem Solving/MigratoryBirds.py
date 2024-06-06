n = int(input())
No_of_Birds = list(map(int, input().split()))
count = {}
for i in No_of_Birds:
    if i not in count.keys():
        count.update({i : 1})
    else:
        count[i] = count[i] + 1
key = []
value = []
temp = []
for i, j in count.items():
    key.append(i)
    value.append(j)
res = max(count.values())
for i in range(len(value)):
    if value[i] == res:
        temp.append(key[i])
print(min(temp))
