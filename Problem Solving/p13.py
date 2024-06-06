n = int(input())
lst_of_inputs = []
s = ''
name = []
email_id = []
new = []
res = []
for i in range(n):
    s = input()
    lst_of_inputs.append(s)
    name.append(0)
    new.append(0)
    email_id.append(0)
    res.append(0)
for i in range(len(lst_of_inputs)):
    new = lst_of_inputs[i].split()
    name[i] = new[0]
    t = new[-1]
    email_id[i] = t[1:-1]
for i in email_id:
    temp = i.split(".")
    ss = temp[0]
    if 0 < len(temp[-1]) < 4:
        if "@" in temp[0]:
            if ss[0].isalpha():
                print("Incomplete")

# #####################INCOMPLETE#####################
