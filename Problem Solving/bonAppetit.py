n = 4
k = 1
bill = [3, 10, 2, 9]
b = 7
total = 0
for i in range(len(bill)):
    if i == k:
        continue
    else:
        total += bill[i]
if int(b - (total/2)) == 0:
    print("Bon Appetit")
else:
    print(int(b - (total/2)))