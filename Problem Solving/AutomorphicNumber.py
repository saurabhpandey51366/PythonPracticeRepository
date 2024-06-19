n = '890625'
num_squared = str(int(n) * int(n))
if num_squared.endswith(n):
    print("Automorphic")
else:
    print("Not Automorphic")