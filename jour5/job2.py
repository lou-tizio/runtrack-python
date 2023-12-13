def draw_rectangle(width, height):
    # Dessiner la première ligne avec des '-'
    print('-' * width)

    # Dessiner les côtés verticaux avec des '|'
    for _ in range(height - 2):
        print('|' + ' ' * (width - 2) + '|')

    # Dessiner la dernière ligne avec des '-'
    if height > 1:
        print('-' * width)

# Appel de la fonction avec les paramètres d'exemple (10, 3)
draw_rectangle(10, 3)