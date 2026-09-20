N = int(input("N: "))
has_two = False
while N > 0:
    if N % 10 == 2:
        has_two = True
    N //= 10
print("TRUE" if has_two else "FALSE")