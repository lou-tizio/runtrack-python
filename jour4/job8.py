L = [8, 24, 27, 48, 2,16, 9, 7, 84, 91]
long = len(L)

#somme des valeurs paires de L
somme = 0
for i in range (long) :
     if L[i] %2 == 0 :
          somme = somme + L[i]
print ("Somme des valeurs paires : ", somme)