import itertools as its
lst = list(map(str, input().split()))
n = int(lst[-1])
l = []
p = []
for i in lst[0]:
    l.append(i)
l.sort()
for i in list(its.permutations(l, n)):
    s = ""
    for j in i:
        s = s + j
    p.append(s)
for i in p:
    print(i)
