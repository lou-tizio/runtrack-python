def decale_message(message, decalage):
    resultat = ''
    for caractere in message:
        if 'a' <= caractere <= 'z':
            nouveau_caractere = chr((ord(caractere) - ord('a') + decalage) % 26 + ord('a'))
            resultat += nouveau_caractere
        elif 'A' <= caractere <= 'Z':
            nouveau_caractere = chr((ord(caractere) - ord('A') + decalage) % 26 + ord('A'))
            resultat += nouveau_caractere
        else:
            resultat += caractere
    return resultat

# Exemple d'utilisation
message_original = "BonjourXYZ"
decalage = 3

message_decale = decale_message(message_original, decalage)
print(f"Message original: {message_original}")
print(f"Message décalé: {message_decale}")
