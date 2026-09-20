N = int(input("N: "))
res = 1.0
while N > 0:
    res *= N
    N -= 2
print("N!! =", res)