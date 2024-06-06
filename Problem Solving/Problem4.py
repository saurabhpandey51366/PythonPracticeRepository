y = int(input())
x = int(input())
flag = 0
count = 0
if y > x:
    print("Not Possible")
else:
    while y != 0 and x != 0:
        temp1 = y % 10
        temp2 = x % 10
        if temp1 > temp2:
            count += 1
            flag = 1
        y = y // 10
        x = x // 10
        temp2 = temp1 = 0
print(count)
