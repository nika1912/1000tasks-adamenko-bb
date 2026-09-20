N = int(input("Введите N: "))
total_sum = 0.0
for i in range(1, N + 1):
    total_sum += 1.0 / i
print(f"Сумма: {total_sum}")