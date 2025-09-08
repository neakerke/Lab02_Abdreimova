a=input("enter your IIN: ")

b = [int(c) for c in a]

# Проход 1: веса 1..11
weights1 = list(range(1, 12))
s1 = sum(d * w for d, w in zip(b, weights1))
C1_int = s1 // 11
k1 = s1 - C1_int * 11

if k1 < 10:
    control = k1
else:
    weights2 = [3,4,5,6,7,8,9,10,11,1,2]
    s2 = sum(d * w for d, w in zip(b, weights2))
    c2_int = s2 // 11
    k2 = s2 - C2_int * 11
    control = k2 if k2 < 10 else 0


print("Razryad:", control)