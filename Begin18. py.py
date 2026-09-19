A = float(input("Введите координату A: "))
B = float(input("Введите координату B: "))
C = float(input("Введите координату C: "))

if C >= A:
    AC = C - A
else:
    AC = A - C

if C >= B:
    BC = C - B
else:
    BC = B - C

print("Длина AC:", AC)
print("Длина BC:", BC)
print("Произведение:", AC * BC)
end='' 
