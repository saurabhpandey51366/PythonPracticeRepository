X = int(input())
shoe_size = list(map(int, input().split()))
N = int(input())
lst_price = []
for i in range(0, N):
    lst = []
    lst = list(map(int, input().split()))
    for j in lst:
        lst_price.append(j)
count_of_shoe_sizes = {}
count_of_bids = {}
for i in shoe_size:
    if i not in count_of_shoe_sizes.keys():
        count_of_shoe_sizes[i] = 1
    else:
        count_of_shoe_sizes[i] = count_of_shoe_sizes[i] + 1
for i in range(0, len(lst_price), 2):
    if lst_price[i] in count_of_bids.keys():
        count_of_bids[lst_price[i]] = count_of_bids[lst_price[i]] + 1
    else:
        count_of_bids.update({lst_price[i]: 1})

# #################INCOMPLETE##############
