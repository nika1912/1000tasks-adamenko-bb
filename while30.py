A = float(input("A: "))
B = float(input("B: "))
C = float(input("C: "))
count = 0
while A >= C and B >= C:
    count += 1
    A -= C
    B -= C
print("Количество:", count)