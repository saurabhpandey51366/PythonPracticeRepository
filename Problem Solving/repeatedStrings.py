s = "a"
n = 100000000000
a_count = 0
for i in s:
    if i == "a":
        a_count += 1
if n > len(s):
    temp = a_count * (int(n / len(s)))
    rem = int(n % len(s))
else:
    temp = a_count * (int(len(s) / n))
    rem = int(len(s) % n)
temp = temp + (a_count * int(rem % len(s)))  
