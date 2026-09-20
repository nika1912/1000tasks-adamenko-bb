A = float(input("A: "))
K = 1
summa = 0.0
while summa <= A:
    summa += 1.0 / K
    K += 1
print("K =", K - 1, "Сумма =", summa)