def fibonnaci_number(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonnaci_number(num - 2) + fibonnaci_number(num - 1)

n = 7
for i in range(0, n):
    print(fibonnaci_number(i), " ", end="")