N = int(input("Введите N: "))
A_prev = 2.0  # A_0

for k in range(1, N + 1):
    A_curr = 2.0 + 1.0 / A_prev
    print(f"A_{k} = {A_curr}")
    A_prev = A_curr