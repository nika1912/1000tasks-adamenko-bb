A = float(input("Введите A: "))
B = float(input("Введите B: "))
C = float(input("Введите C: "))

D = B * B - 4 * A * C

x1 = (-B - D ** 0.5) / (2 * A)
x2 = (-B + D ** 0.5) / (2 * A)

if x1 < x2:
    print(x1)
    print(x2)
else:
    print(x2)
    print(x1)B = float(input("Введите B: "))

x = -B / A

print("x =", x)
end = ""
