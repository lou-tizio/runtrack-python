L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
values = 1
for i in range (0, len (L)) :
    if 25 <= L [i] <= 90 :
        values = values*L[i]
print(f"produit des valeurs comprises entre 25 et 90 : {values}")