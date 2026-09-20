N = int(input("Введите N: "))
total_sum = 0.0

for i in range(1, N + 1):
    exponent = N - i + 1
    total_sum += i ** exponent

print(f"Сумма: {total_sum}")