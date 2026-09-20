N = int(input("Введите N: "))
product = 1.0
for i in range(1, N + 1):
    product *= (1.0 + i / 10.0)
print(f"Произведение: {product}")