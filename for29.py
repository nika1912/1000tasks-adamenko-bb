N = int(input("Введите N: "))
A = float(input("Введите A: "))
B = float(input("Введите B: "))

H = (B - A) / N
print(f"Длина отрезка H = {H}")

for i in range(N + 1):
    point = A + i * H
    print(f"Точка {i}: {point}")