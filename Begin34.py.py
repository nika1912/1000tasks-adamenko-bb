X = float(input("Введите X (кг шоколадных): "))
A = float(input("Введите A (рублей): "))
Y = float(input("Введите Y (кг ирисок): "))
B = float(input("Введите B (рублей): "))

price_choc = A / X
price_toffee = B / Y
diff = price_choc / price_toffee

print("1 кг шоколадных конфет:", price_choc)
print("1 кг ирисок:", price_toffee)
print("Шоколадные дороже в", diff, "раз")
end = ""
