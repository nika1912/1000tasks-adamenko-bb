N = int(input("N: "))
f1, f2 = 1, 1
while f2 < N:
    f1, f2 = f2, f1 + f2
print("Предыдущее:", f1, "Следующее:", f1 + f2)