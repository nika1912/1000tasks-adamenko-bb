N = int(input("Введите N: "))
total_sum = 0.0
current_fact = 1.0
for i in range(1, N + 1):
    current_fact *= i
    total_sum += current_fact
print(f"Сумма факториалов: {total_sum}")