import math
X = float(input("Введите X: "))
N = int(input("Введите N: "))
result = 0.0
current_power = X
current_fact = 1.0
for i in range(1, N + 1):
    # Вычисляем факториал для (2i-1)!
    if i > 1:
        current_fact *= (2 * i - 2) * (2 * i - 1)
    else:
        current_fact = 1.0 # 1! = 1
        
    term = current_power / current_fact
    if i % 2 == 1:
        result += term
    else:
        result -= term
    current_power *= X * X
print(f"Значение sin({X}): {result}")