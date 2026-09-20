A = int(input("Введите A: "))
B = int(input("Введите B: "))
count = 0
for i in range(A, B + 1):
    print(i)
    count += 1
print(f"Количество чисел: {count}")