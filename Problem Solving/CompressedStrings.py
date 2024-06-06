s = 'abacaaabbb'
len_str = len(s)
new_str = ''
i = 0
while i != len_str:
    count = 1
    while i < len_str - 1 and s[i] == s[i + 1]:
        count += 1
        i += 1
    if count == 1:
        new_str += str(s[i])
        print(str(s[i]))
    else:
        new_str += str(s[i]) + str(count)
        print(str(s[i]))
    i += 1
print(new_str)
