def factorial(num):
    temp = 1
    for i in range(1, num+1):
        temp *= i
    return temp


n = 10
print(factorial(n-1) * 2)
