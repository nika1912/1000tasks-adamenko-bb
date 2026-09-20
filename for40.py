A = int(input("Введите A: "))
B = int(input("Введите B: "))

count = 1
for i in range(A, B + 1):
    for _ in range(count):
        print(i)
    count += 1