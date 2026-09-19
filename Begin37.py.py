V1 = float(input())
V2 = float(input())
S = float(input())
T = float(input())

S_total = S - (V1 + V2) * T

if S_total < 0:
    S_total = -S_total

print(S_total)
end = ""
