e = float(input("e: "))
A1 = 1.0
A2 = 2.0
K = 3
while True:
    A3 = (A1 + 2 * A2) / 3.0
    if abs(A3 - A2) < e:
        break
    A1, A2 = A2, A3
    K += 1
print("K =", K, "A_{k-1} =", A2, "A_k =", A3)