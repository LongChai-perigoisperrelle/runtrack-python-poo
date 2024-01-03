class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    # Assesseurs (getters)
    def get_longueur(self):
        return self.__longueur

    def get_largeur(self):
        return self.__largeur

    # Mutateurs (setters)
    def set_longueur(self, longueur):
        self.__longueur = longueur

    def set_largeur(self, largeur):
        self.__largeur = largeur

    # Méthode pour calculer l'aire du rectangle
    def calculer_aire(self):
        return self.__longueur * self.__largeur

# Création d'un rectangle avec les valeurs initiales
mon_rectangle = Rectangle(10, 5)

# Affichage des valeurs initiales
print(f"Longueur initiale : {mon_rectangle.get_longueur()}")
print(f"Largeur initiale : {mon_rectangle.get_largeur()}")
print(f"Aire initiale : {mon_rectangle.calculer_aire()}")

# Modification des valeurs
mon_rectangle.set_longueur(15)
mon_rectangle.set_largeur(8)

# Affichage des nouvelles valeurs
print(f"\nLongueur modifiée : {mon_rectangle.get_longueur()}")
print(f"Largeur modifiée : {mon_rectangle.get_largeur()}")
print(f"Aire modifiée : {mon_rectangle.calculer_aire()}")