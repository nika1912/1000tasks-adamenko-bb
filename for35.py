N = int(input("Введите N: "))

if N >= 1:
    print("A_1 = 1")
if N >= 2:
    print("A_2 = 2")
if N >= 3:
    print("A_3 = 3")

A1 = 1
A2 = 2
A3 = 3

for k in range(4, N + 1):
    A_curr = A3 + A2 - 2 * A1
    print(f"A_{k} = {A_curr}")
    A1 = A2
    A2 = A3
    A3 = A_curr