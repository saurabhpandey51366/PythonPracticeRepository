# class Result:
#
#     def new_func(self, marks):
#         if marks >= 90:
#             return 'A'
#         elif marks >= 80:
#             return 'B'
#         else:
#             return 'C'
#
#
# obj = Result()
#
# print(obj.new_func(100))
n = 10
summ = 0
res = 0
for i in range(1, n+1, 2):
    for j in range(i, i+3):
        summ = summ + j
    res = res + summ
    summ = 0
print(res)