import math

N = int(input("Введите N: "))
A = float(input("Введите A: "))
B = float(input("Введите B: "))

H = (B - A) / N
print(f"Длина отрезка H = {H}")

for i in range(N + 1):
    X = A + i * H
    F = 1 - math.sin(X)
    print(f"F({X}) = {F}")