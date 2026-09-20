N = int(input("Введите N: "))
total_sum = 0.0

for i in range(1, N + 1):
    total_sum += i ** i

print(f"Сумма: {total_sum}")