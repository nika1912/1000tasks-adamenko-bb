N = int(input("Введите N: "))
result = 0.0
sign = 1.0
for i in range(1, N + 1):
    term = 1.0 + i / 10.0
    result += sign * term
    sign = -sign
print(f"Значение: {result}")