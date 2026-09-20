N = int(input("Введите N: "))
K = int(input("Введите K: "))
total_sum = 0.0

for i in range(1, N + 1):
    total_sum += i ** K

print(f"Сумма: {total_sum}")