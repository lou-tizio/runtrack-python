def afficher_tapis_diagonale(n):
    for i in range(n+1):
        for j in range(n+1):
            if i == j:
                print('#', end='')
            elif i + j == n:
                print('#', end='')
            else:
                print('_', end='')
        print()

# Demander à l'utilisateur la taille du tapis
taille_tapis = int(input("Entrez la taille du tapis : "))

# Appel de la fonction avec la taille spécifiée
afficher_tapis_diagonale(taille_tapis)
