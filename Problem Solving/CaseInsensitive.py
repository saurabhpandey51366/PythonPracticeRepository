print("Enter your Choice:\n1. Uppercase\n2. Lowercase\n3. Capitalize\n4. Toggle Case")
ch = int(input())

lst = []

def toUpperCase(i):
    if 64 < ord(i) < 91:
        return i
    else:
        return chr(ord(i) - 32)


def toLowerCase(i):
    if 64 < ord(i) < 91:
        return chr(ord(i) + 32)
    else:
        return i


print("Enter the String:")
s = input()

if ch == 1:
    for i in s:
        lst.append(toUpperCase(i))

elif ch == 2:
    for i in s:
        lst.append(toLowerCase(i))

elif ch == 3:
    for i in range(len(s)):
        if i == 0:
            lst.append(toUpperCase(s[i]))
        else:
            lst.append(toLowerCase(s[i]))

elif ch == 4:
    for i in s:
        if 64 < ord(i) < 91:
            lst.append(toLowerCase(i))
        else:
            lst.append(toUpperCase(i))

s = ''
for i in lst:
    s += i
print(s)
