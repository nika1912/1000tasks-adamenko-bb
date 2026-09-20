X = float(input("Введите X: "))
N = int(input("Введите N: "))
result = 1.0
current_fact = 1.0
current_power = 1.0
for i in range(1, N + 1):
    current_power *= X
    current_fact *= i
    result += current_power / current_fact
print(f"Значение exp({X}): {result}")