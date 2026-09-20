N = int(input("N: "))
K = 1
summa = 0
while summa < N:
    summa += K
    K += 1
print("K =", K - 1, "Сумма =", summa)