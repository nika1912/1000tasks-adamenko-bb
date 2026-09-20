N = int(input("Введите N: "))
factorial = 1.0
for i in range(1, N + 1):
    factorial *= i
print(f"{N}! = {factorial}")