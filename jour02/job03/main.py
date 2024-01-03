class Livre:
    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur
        self.disponible = True  # attribut privé initialisé à True par défaut

    def verification(self):
        # Méthode pour vérifier si le livre est disponible
        return self.disponible

    def emprunter(self):
        # Méthode pour emprunter le livre
        if self.verification():  # Vérifie si le livre est disponible
            self.disponible = False
            print(f"Le livre '{self.titre}' a été emprunté avec succès.")
        else:
            print(f"Le livre '{self.titre}' n'est pas disponible pour l'emprunt.")

    def rendre(self):
        # Méthode pour rendre le livre
        if not self.verification():  # Vérifie si le livre a été emprunté
            self.disponible = True
            print(f"Le livre '{self.titre}' a été rendu avec succès.")
        else:
            print(f"Le livre '{self.titre}' n'a pas été emprunté, donc ne peut pas être rendu.")

# Exemple d'utilisation
livre1 = Livre("Harry Potter", "J.K. Rowling")

# Vérification de la disponibilité du livre
print(f"Le livre '{livre1.titre}' est disponible : {livre1.verification()}")

# Emprunt du livre
livre1.emprunter()

# Tentative d'emprunt du livre déjà emprunté
livre1.emprunter()

# Rendre le livre
livre1.rendre()

# Tentative de rendre le livre déjà rendu
livre1.rendre()