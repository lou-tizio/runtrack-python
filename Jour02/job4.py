# somme de 2 nombre
# num1 = 12
# num2 = 34
# somme = num1 + num2
# print(f"la somme est {somme}")

# nbr = 5
# somme = nbr + 1 + 2 + 3 + 4 + 5
# print(f"la somme est {somme}")

# tableau = [1,2,3,4,5]
# somme = nbr
# for item in tableau:
#     somme += item
# somme = nbr
print("veiller saissir un nombre entier superieur a zero")
nbre = input()
nbreToint = int(nbre)

#Creer un tableau dynamique pour valeur à multiplier, si utilisateur saisi 3 alors table 
# de mutiplication de 1 à 3. je fais n+1 car range c'est [1,n[
multiplyTo = range(1, nbreToint+1)
for value in range(1, nbreToint+1):
    print(f"table de multiplication par {value}")
    for item in range(1, 11):
      somme = value * item
      print(f"{value} * {item} =  {somme}")

    
    



