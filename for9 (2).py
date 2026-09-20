A = int(input("Введите A: "))
B = int(input("Введите B: "))
sum_sq = 0
for i in range(A, B + 1):
    sum_sq += i ** 2
print(f"Сумма квадратов: {sum_sq}")