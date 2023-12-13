def draw_triangle(height):
    for i in range(height):
        spaces = ' ' * (height - i - 1)
        if i == 0:
            print(spaces)
        else:
            left_slash ='/'
            right_slash ='\\'
            middle_spaces = ' ' * (2 * i - 1)
            print(spaces + left_slash + middle_spaces + right_slash)
            
        
# Demander à l'utilisateur la hauteur du triangle
hauteur = int(input("Entrez la hauteur du triangle : "))

# Appel de la fonction avec la hauteur spécifiée
draw_triangle(hauteur)
