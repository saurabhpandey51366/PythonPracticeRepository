lst = list(map(str, input().split()))
number = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
res = []
for i in lst:
    for j in number:
        if i == j:
            res.append(number.index(j))
for i in res:
    print(i, end="")
