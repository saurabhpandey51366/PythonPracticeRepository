n = 6
p = 2
eve = []
odd = []
count = []
for i in range(n):
    if i % 2 == 0:
        eve.append(i)
    else:
        odd.append(i)
for i in range(max(len(eve), len(odd))):
    count[i] = 1

