s = [3, 6, 8, 10]
max_num = max(s)
num = max_num
while True:
    lst = [num % i for i in s]
    if all(v == 0 for v in lst):
        temp = num
        break
    else:
        lst.clear()
    num += max_num
print(temp)