N = int(input("Введите N: "))
A_prev = 1.0  # A_0

for k in range(1, N + 1):
    A_curr = (A_prev + 1.0) / k
    print(f"A_{k} = {A_curr}")
    A_prev = A_curr