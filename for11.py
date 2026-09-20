N = int(input("Введите N: "))
total_sum = 0
for i in range(0, N + 1):
    total_sum += (N + i) ** 2
print(f"Сумма: {total_sum}")