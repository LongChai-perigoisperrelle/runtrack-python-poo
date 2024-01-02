class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        print(f"Coordonnées du point : ({self.x}, {self.y})")

    def afficherX(self):
        print(f"Coordonnée horizontale (x) : {self.x}")

    def afficherY(self):
        print(f"Coordonnée verticale (y) : {self.y}")

    def changerX(self, nouveauX):
        self.x = nouveauX

    def changerY(self, nouveauY):
        self.y = nouveauY


# Exemple d'utilisation
point1 = Point(2, 3)
point1.afficherLesPoints()
point1.afficherX()
point1.afficherY()

point1.changerX(5)
point1.changerY(7)

point1.afficherLesPoints()