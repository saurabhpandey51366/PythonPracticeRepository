n = int(input())
lst_ph_num = []
temp = []
count = 0
for i in range(0, n):
    lst_ph_num.append(input())
    temp.append(2)
for i in lst_ph_num:
    for j in i:
        if j.isalpha():
            temp[count] = -1
            break
        else:
            temp[count] = 0
    count += 1
count = 0
for i in lst_ph_num:
    res = i[0]
    if temp[count] == 0:
        if len(i) == 10:
            if int(res) == 7 or int(res) == 8 or int(res) == 9:
                print("YES")
            else:
                print("NO")
        else:
            print("NO")
    else:
        print("NO")
    count += 1
