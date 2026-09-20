N = int(input("N: "))
has_odd = False
while N > 0:
    if (N % 10) % 2 != 0:
        has_odd = True
    N //= 10
print("TRUE" if has_odd else "FALSE")