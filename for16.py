A = float(input("Введите A: "))
N = int(input("Введите N: "))
current_power = 1.0
for i in range(1, N + 1):
    current_power *= A
    print(f"A в степени {i} = {current_power}")