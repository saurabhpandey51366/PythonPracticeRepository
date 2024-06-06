ar = [6, 0, 1, 8, 0, 2]
for i in ar:
    if i == 0:
        ar.remove(i)
        ar.append(0)
print(ar)