# from forex_python.converter import CurrencyRates

# def convert_currency(amount, from_currency, to_currency):
#     # Créer une instance de la classe CurrencyRates
#     c = CurrencyRates()

#     try:
#         # Obtenir le taux de change
#         exchange_rate = c.get_rate(from_currency, to_currency)

#         # Calculer le montant converti
#         converted_amount = amount * exchange_rate

#         # Afficher les résultats
#         print(f"{amount} {from_currency} équivaut à {converted_amount:.2f} {to_currency}")

#     except Exception as e:
#         print(f"Une erreur s'est produite : {e}")

# if __name__ == "__main__":
#     # Demander à l'utilisateur les détails de la conversion
#     amount = float(input("Entrez le montant à convertir : "))
#     from_currency = input("Entrez la devise source (code ISO, par exemple USD) : ").upper()
#     to_currency = input("Entrez la devise cible (code ISO, par exemple EUR) : ").upper()

#     # Appeler la fonction pour effectuer la conversion
#     convert_currency(amount, from_currency, to_currency)

from forex_python.converter import CurrencyRates
import json

class CurrencyConverter:
    def __init__(self):
        self.c = CurrencyRates()
        self.history = []

    def convert_currency(self, amount, from_currency, to_currency):
        try:
            # Obtenir le taux de change
            exchange_rate = self.c.get_rate(from_currency, to_currency)

            # Calculer le montant converti
            converted_amount = amount * exchange_rate

            # Ajouter la conversion à l'historique
            self.history.append({
                'amount': amount,
                'from_currency': from_currency,
                'to_currency': to_currency,
                'converted_amount': converted_amount
            })

            # Afficher les résultats
            print(f"{amount} {from_currency} équivaut à {converted_amount:.2f} {to_currency}")

        except Exception as e:
            print(f"Une erreur s'est produite : {e}")

    def add_custom_currency(self, currency, conversion_rate):
        # Ajouter une nouvelle devise personnalisée
        self.c.add_rate('USD', currency, conversion_rate)

if __name__ == "__main__":
    converter = CurrencyConverter()

    while True:
        print("\n1. Convertir une somme")
        print("2. Ajouter une devise personnalisée")
        print("3. Afficher l'historique des conversions")
        print("4. Quitter")

        choice = input("Choisissez une option (1/2/3/4) : ")

        if choice == '1':
            amount = float(input("Entrez le montant à convertir : "))
            from_currency = input("Entrez la devise source (code ISO, par exemple USD) : ").upper()
            to_currency = input("Entrez la devise cible (code ISO, par exemple EUR) : ").upper()
            converter.convert_currency(amount, from_currency, to_currency)

        elif choice == '2':
            custom_currency = input("Entrez le code ISO de la nouvelle devise : ").upper()
            conversion_rate = float(input("Entrez le taux de conversion par rapport à l'USD : "))
            converter.add_custom_currency(custom_currency, conversion_rate)
            print(f"La devise {custom_currency} a été ajoutée avec succès.")

        elif choice == '3':
            print("\nHistorique des conversions :")
            for entry in converter.history:
                print(entry)

        elif choice == '4':
            break

        else:
            print("Option invalide. Veuillez réessayer.")
