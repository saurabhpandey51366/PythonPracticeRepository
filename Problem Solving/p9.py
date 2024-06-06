lst_A = list(map(int, input().split()))
lst_B = list(map(int, input().split()))
res = ""
lst = []
for i in lst_A:
    for j in lst_B:
        lst.append("(" + str(i) + ", " + str(j) + ")")
for i in lst:
    if i == lst[-1]:
        res = res + i
    elif ")" in i:
        res = res + i + " "
    else:
        res = res + i
print(res)

