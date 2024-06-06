import math
s = '4576'
quo = -1
rem = []
while quo != 0:
    rem.append(int(s) % 2)
    quo = int(s) / 2
    s = int(quo)
rem.reverse()
y = ''
for i in rem:
    y = y + str(i)
print(y)