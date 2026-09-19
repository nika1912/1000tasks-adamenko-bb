X = float(input("Введите X (кг): "))
A = float(input("Введите A (рублей): "))
Y = float(input("Введите Y (кг): "))

price1 = A / X
priceY = price1 * Y

print("Стоимость 1 кг:", price1)
print("Стоимость", Y, "кг:", priceY)
end = ""
