A = float(input("Введите A: "))
N = int(input("Введите N: "))
result = 0.0
current_power = 1.0
sign = 1.0
for i in range(0, N + 1):
    result += sign * current_power
    current_power *= A
    sign = -sign
print(f"Значение: {result}")