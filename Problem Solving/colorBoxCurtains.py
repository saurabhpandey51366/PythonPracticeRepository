s = "abbbaabbb"
l = 5
stList = []
temp = ''
for i in range(1, len(s)+1):
    temp += s[i-1]
    if i % l == 0:
        stList.append(temp)
        temp = ''
res = len(s) % l
stList.append(s[len(s) - res:])
count = 0
mx = -1
for i in stList:
    for j in i:
        if j == 'a':
            count += 1
    if count > mx:
        mx = count
    count = 0
print(mx)
