class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix

    def informationsVehicule(self):
        print(f"Marque: {self.marque}")
        print(f"Modèle: {self.modele}")
        print(f"Année: {self.annee}")
        print(f"Prix: {self.prix} €")


class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix, portes=4):
        super().__init__(marque, modele, annee, prix)
        self.portes = portes

    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de portes: {self.portes}")


class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix, roues=2):
        super().__init__(marque, modele, annee, prix)
        self.roues = roues

    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de roues: {self.roues}")


# Création d'une voiture
voiture = Voiture("Toyota", "Corolla", 2022, 25000)

# Affichage des informations de la voiture
voiture.informationsVehicule()

# Création d'une moto
moto = Moto("Harley-Davidson", "Sportster", 2021, 12000)

# Affichage des informations de la moto
moto.informationsVehicule()

# Méthode de démarrage
class Vehicule:
    def demarrer(self):
        print("Attention, je roule")

class Voiture(Vehicule):
    def demarrer(self):
        print("Vroom! La voiture démarre.")

class Moto(Vehicule):
    def demarrer(self):
        print("Vrooom! La moto démarre.")

# Création d'une voiture et d'une moto
voiture = Voiture()
moto = Moto()

# Démarrage des véhicules
voiture.demarrer()
moto.demarrer()