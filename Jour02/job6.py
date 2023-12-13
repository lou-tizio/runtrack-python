
print("les nombre de 0 à 1000 sont : ")
for item in range (0, 1001) :
    isNbPremier = True
    if item >= 2 :
          diviseur = 2
          while diviseur < item :
             if item % diviseur == 0 :
                isNbPremier = False
                break
             diviseur +=1
          if isNbPremier:
            print(f"{item}")

