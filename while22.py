N = int(input("N: "))
is_prime = True
i = 2
while i * i <= N:
    if N % i == 0:
        is_prime = False
        break
    i += 1
print("TRUE" if is_prime and N > 1 else "FALSE")