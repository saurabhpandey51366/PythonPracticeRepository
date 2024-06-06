day = "mon"
no_of_days = 13
count = 0
DOW = {"mon": 1, "tue": 2, "wed": 3, "thu": 4, "fri": 5, "sat": 6, "sun": 7}
for i in range(DOW[day], DOW[day] + no_of_days):
    if i % 7 == 0:
        count += 1
    print(i)
print(count)