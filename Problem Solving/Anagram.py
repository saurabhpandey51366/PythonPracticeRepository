s = 'abcdef'
q = 'bdz'
temp = -1
for i in q:
    if i not in s:
        temp = 0
if temp == 0:
    print('Not an Anagram')
else:
    print('Anagram')
