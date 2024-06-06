a = "796115110113721110141108"
i = 0
while i<len(a)-1:
    if (int(a[i]+a[i+1])>64 and int(a[i]+a[i+1]<91)) or (int(a[i]+a[i+1])>96 and int(a[i]+a[i+1])<101):
        s = int(a[i]+a[i+1])
    