prices = [7, 1, 5, 4, 3, 8, 10]
res = []
for i, j in enumerate(prices):
    if len(prices[i+1:]) > 0:
        if j > max(prices[i+1:]):
            continue
        else:
            res.append(max(prices[i+1:]) - j)
print(max(res))