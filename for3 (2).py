A = int(input("Введите A: "))
B = int(input("Введите B: "))
count = 0
for i in range(B - 1, A, -1):
    print(i)
    count += 1
print(f"Количество чисел: {count}")