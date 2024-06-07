x = input()
for i in range(x):
    for j in range(x):
        if i == 0 or i == x or j == 0 or j == x:
            print("#", end="")
        elif i == j or i + j == x - 1:
            print("#", end="")
        else:
            print(" ", end="")
    print("")
