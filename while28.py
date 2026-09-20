e = float(input("e: "))
A_prev = 2.0
A_curr = 2.0 + 1.0 / A_prev
K = 2
while abs(A_curr - A_prev) >= e:
    A_prev = A_curr
    A_curr = 2.0 + 1.0 / A_prev
    K += 1
print("K =", K, "A_prev =", A_prev, "A_curr =", A_curr)