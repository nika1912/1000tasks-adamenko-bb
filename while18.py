N = int(input("N: "))
count = 0
summa = 0
while N > 0:
    summa += N % 10
    N //= 10
    count += 1
print("Количество:", count, "Сумма:", summa)