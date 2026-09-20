A = float(input("Введите A: "))
N = int(input("Введите N: "))
total_sum = 0.0
current_power = 1.0
for i in range(0, N + 1):
    total_sum += current_power
    current_power *= A
print(f"Сумма: {total_sum}")