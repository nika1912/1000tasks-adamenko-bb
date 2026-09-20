N = int(input("Введите N: "))
current_sum = 0
for i in range(1, N + 1):
    odd_num = 2 * i - 1
    current_sum += odd_num
    print(f"Квадрат {i} равен {current_sum}")