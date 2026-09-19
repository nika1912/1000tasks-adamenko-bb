x1 = float(input("Введите x1: "))
y1 = float(input("Введите y1: "))
x2 = float(input("Введите x2: "))
y2 = float(input("Введите y2: "))

if x2 >= x1:
    a = x2 - x1
else:
    a = x1 - x2

if y2 >= y1:
    b = y2 - y1
else:
    b = y1 - y2

P = 2 * (a + b)
S = a * b

print("Периметр:", P)
print("Площадь:", S)
end='' 
