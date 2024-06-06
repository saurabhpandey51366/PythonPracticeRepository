s = '###***#**'
sharp_count = 0
star_count = 0
for i in s:
    if i == '#':
        sharp_count += 1
    elif i == '*':
        star_count += 1
print(sharp_count - star_count)
