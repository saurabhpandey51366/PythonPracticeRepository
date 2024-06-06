a = 10
a_bin = bin(a)[2:]
res = []
s = ''
final = 0
count = 0
for i in a_bin:
    if i == '0':
        res.append('1')
    else:
        res.append('0')
for i in res:
    s = s + i
for i in s[::-1]:
    if count == len(s)-1:
        if i == '1':
            final += 1
    else:
        if i == '1':
            final += pow(2, count)
    count += 1
print(final)