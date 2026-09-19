x1 = float(input("Введите x1: "))
y1 = float(input("Введите y1: "))
x2 = float(input("Введите x2: "))
y2 = float(input("Введите y2: "))
x3 = float(input("Введите x3: "))
y3 = float(input("Введите y3: "))

a = ((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1)) ** 0.5
b = ((x3 - x2) * (x3 - x2) + (y3 - y2) * (y3 - y2)) ** 0.5
c = ((x1 - x3) * (x1 - x3) + (y1 - y3) * (y1 - y3)) ** 0.5

print("Сторона a:", a)
print("Сторона b:", b)
print("Сторона c:", c)

P = a + b + c
p = P / 2

print("Периметр:", P)
print("Полупериметр:", p)

S = (p * (p - a) * (p - b) * (p - c)) ** 0.5

print("Площадь:", S)
end='' 
