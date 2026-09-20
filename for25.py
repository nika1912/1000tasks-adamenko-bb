X = float(input("Введите X (|X|<1): "))
N = int(input("Введите N: "))
result = 0.0
current_power = X
for i in range(1, N + 1):
    term = current_power / i
    if i % 2 == 1:
        result += term
    else:
        result -= term
    current_power *= X
print(f"Значение ln(1+{X}): {result}")