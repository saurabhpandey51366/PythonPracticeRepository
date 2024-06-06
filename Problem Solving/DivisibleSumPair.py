n = int(input())
ar = list(map(int, input().split()))
k = int(input())
pairs = []
for i in ar:
    for j in ar:
        if i == j:
            continue
        else:
            if (i + j) % k == 0:
                print(i, j)
