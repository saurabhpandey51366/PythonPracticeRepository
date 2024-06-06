m = int(input())
n = int(input())
arr = []
for i in range(0, m):
    ar = []
    ar = list(map(int, input().split()))
    for j in ar:
        arr.append(j)
for i in range(0, m):
    print(max(arr[n*i:(n*i)+n]), end=" ")