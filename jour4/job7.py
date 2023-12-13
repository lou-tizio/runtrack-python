L = [8, 24, 48, 2, 16]

long = len(L)

multiply = 0
for i in range (long):
    if L[i] % 3 == 0 :
        multiply = multiply + 1
print("nombre de multiples de 3 : ", multiply)
    