v = 200
w = 540
if w % 2 == 0 and w >= 2 and w > v:
    res_four = (w - (2 * v)) // 2
    print(200 - res_four, res_four)
else:
    print('INVALID INPUT')
