X = float(input("Введите X (|X|<1): "))
N = int(input("Введите N: "))
result = X
current_power = X
current_num = 1.0
current_den = 1.0
for i in range(1, N + 1):
    current_num *= (2 * i - 1)
    current_den *= (2 * i)
    term = (current_power * X * X) * (current_num / current_den) / (2 * i + 1)
    result += term
print(f"Значение arcsin({X}): {result}")