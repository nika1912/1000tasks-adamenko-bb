P = float(input("P: "))
day_dist = 10.0
total_dist = 0.0
days = 0
while total_dist <= 200:
    total_dist += day_dist
    day_dist *= (1 + P / 100)
    days += 1
print("Дней:", days, "Суммарно:", total_dist)