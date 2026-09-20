X = float(input("Введите X: "))
N = int(input("Введите N: "))
result = 1.0
current_power = 1.0
current_fact = 1.0
for i in range(1, N + 1):
    current_power *= X * X
    current_fact *= (2 * i - 1) * (2 * i)
    term = current_power / current_fact
    if i % 2 == 1:
        result -= term
    else:
        result += term
print(f"Значение cos({X}): {result}")