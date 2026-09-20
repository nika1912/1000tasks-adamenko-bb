ddX = float(input("Введите X (|X|<1): "))
N = int(input("Введите N: "))
result = 1.0
current_power = X
current_num = 1.0
current_den = 2.0
for i in range(1, N + 1):
    if i == 1:
        coeff = 1.0 / 2.0
    else:
        coeff = (current_num / current_den) / 2.0
    
    term = coeff * current_power
    if i % 2 == 1:
        result -= term
    else:
        result += term
        
    current_num *= (2 * i - 1)
    current_den *= (2 * i + 2)
    current_power *= X

print(f"Значение sqrt(1+{X}): {result}")