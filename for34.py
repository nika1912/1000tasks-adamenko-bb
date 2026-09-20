N = int(input("Введите N: "))

if N >= 1:
    print("A_1 = 1")
if N >= 2:
    print("A_2 = 2")

A_k_minus_2 = 1.0
A_k_minus_1 = 2.0

for k in range(3, N + 1):
    A_curr = (A_k_minus_2 + 2.0 * A_k_minus_1) / 3.0
    print(f"A_{k} = {A_curr}")
    A_k_minus_2 = A_k_minus_1
    A_k_minus_1 = A_curr