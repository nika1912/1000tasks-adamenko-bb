P = float(input("P: "))
summa = 1000.0
months = 0
while summa <= 1100:
    summa *= (1 + P / 100)
    months += 1
print("Месяцев:", months, "Итог:", summa)