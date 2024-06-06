# def elemRemover(arr, i):
#     for j in range(0, len(arr)):
#         if j == i:
#             continue
#         else:
#             temp.append(arr[j])
#     return temp
# m = int(input())
# arr = []
# temp = []
# dictt = {}
# for i in range(0, m):
#     arr.append(input())
#     dictt[arr[i]] = 0
# res = [arr[0]]
# for i in range(1, m):
#     temp = elemRemover(arr, i)
#     print("Temp Array: ", temp, "i: ", i)
#     if arr[i] in temp:
#         res.append(arr[i]+str())
#     else:
#         res.append(arr[i])
#     temp = []
# print(res)

n=int(input())
arr = []
ans = ""
for i in range(n):
    arr.append(input())
print()
for i in range(n):
    if arr[:i+1].count(arr[i])>1:
        ans = arr[i]+str(arr[:i+1].count(arr[i])-1)
    else:
        ans = arr[i]
    print(ans)