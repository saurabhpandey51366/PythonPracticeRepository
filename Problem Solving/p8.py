s = "alison heck"
lst = []
for i in range(0, len(s)):
    if i == 0:
        if s[i].islower():
            lst.append(s[i].upper())
        else:
            lst.append(s[i])
    elif s[i-1] == " ":
        lst.append(s[i].upper())
    else:
        lst.append(s[i])
new_s = ""
for i in lst:
    new_s = new_s + i
print(new_s)
