N = int(input("Введите N: "))

if N >= 1:
    print("F_1 = 1")
if N >= 2:
    print("F_2 = 1")

F_k_minus_2 = 1  
F_k_minus_1 = 1  

for k in range(3, N + 1):
    F_curr = F_k_minus_1 + F_k_minus_2
    print(f"F_{k} = {F_curr}")
    F_k_minus_2 = F_k_minus_1
    F_k_minus_1 = F_curr