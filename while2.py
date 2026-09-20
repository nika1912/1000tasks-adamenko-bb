A = float(input("A: "))
B = float(input("B: "))
count = 0
while A >= B:
    A -= B
    count += 1
print("Количество:", count)