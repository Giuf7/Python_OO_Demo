class voiture:
    voitures_crees = 0
    def __init__(self, marque):
        self.marque = marque
        voiture.voitures_crees += 1
    # couleur = "rouge"

    def afficher_marque(self):
        print("La marque est :", self.marque)

# print("La marque est :", voiture.marque)
# print("La couleur est :", voiture.couleur)

voiture_01 = voiture("Lamborghini")
voiture_02 = voiture("Ferrari")

voiture_01.afficher_marque()
voiture_02.afficher_marque()
print("Nombre de voitures créées :", voiture.voitures_crees)
# voiture.afficher_marque(voiture_01)

# voiture.marque = "Porsche"

# print("Voiture 01 - Marque :", voiture_01.marque)
# print("Voiture 02 - Marque :", voiture_02.marque)

# voiture_01.marque = "Peugeot"
# voiture_02.marque = "Volkswagen"

# print(voiture.marque)
# print(voiture_01.marque)
# print(voiture_02.marque)

# Classe
class voiture:
    # Attribut de classe
    pneus = 4

    # Méthode
    def __init__(self, marque):
        # Attribut d'instance
        self.marque = marque

# Instance
lamborghini = voiture("Lamborghini")