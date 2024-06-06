# n = 31
# def lst_to_int(num):
#     s = ''
#     for i in num:
#         s = s + str(i)
#     return s
# def dec_to_oct(n):
#     rem = []
#     temp = n
#     while temp != 0:
#         rem.append(temp % 8)
#         temp = int(temp / 8)
#     rem.reverse()
#     return lst_to_int(rem)
# def dec_to_bin(n):
#     rem = []
#     temp = n
#     while temp != 0:
#         rem.append(temp % 2)
#         temp = int(temp / 2)
#     rem.reverse()
#     return lst_to_int(rem)
# def dec_to_hex(n):
#     rem = []
#     temp = n
#     hexTable = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
#     while temp != 0:
#         rem.append(temp % 16)
#         temp = int(temp / 16)
#     for i in range(len(rem)):
#         if rem[i] in hexTable.keys():
#             rem[i] = hexTable[rem[i]]
#     rem.reverse()
#     return lst_to_int(rem)
# lstOct2 = []
# lstHex2 = []
# lstBin2 = []
# for i in range(1, n):
#     lstOct2.append(dec_to_oct(i))
#     lstBin2.append(dec_to_bin(i))
#     lstHex2.append(dec_to_hex(i))
#     print(i-1, "\t", lstOct2[i-1], "\t", lstHex2[i-1], "\t", lstBin2[i-1])
def hex_printer(s):
    temp = ''
    for i in s:
        if i.islower():
            temp  = temp + i.upper()
        else:
            temp = temp + i
    return temp

max_dec_len = len(str(int(n)))
max_oct_len = len(str(oct(n)))-2
max_hex_len = len(str(hex(n)))-2
max_bin_len = len(str(bin(n)))-2

for i in range(1, n+1):
    oc = str(oct(i))
    he = str(hex(i))
    bi = str(bin(i))
    s = ' '
    print((max_dec_len-len(str(i)))*s, end="")
    print(i, s*(max_oct_len-len(oc[2:])), oc[2:], s*(max_hex_len-len(he[2:])), hex_printer(he[2:]), s*(max_bin_len-len(bi[2:])), bi[2:])
