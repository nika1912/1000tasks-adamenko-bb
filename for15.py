A = float(input("Введите A: "))
N = int(input("Введите N: "))
result = 1.0
for _ in range(N):
    result *= A
print(f"A в степени N: {result}")