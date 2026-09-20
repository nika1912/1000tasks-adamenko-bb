N = int(input("N: "))
f1, f2 = 1, 1
k = 2
while f2 < N:
    f1, f2 = f2, f1 + f2
    k += 1
print("Номер:", k)