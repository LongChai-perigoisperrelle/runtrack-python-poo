class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def bonjour(self):
        print(f"Bonjour, je m'appelle {self.nom}.")

class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours.")

    # Redéfinir l'âge de l'élève à 15 ans
    def setAge(self, age):
        self.age = age

class Professeur(Personne):
    def enseigner(self):
        print(f"{self.nom} commence le cours.")

# Créer un objet élève
eleve1 = Eleve("Jerome", 15)

# Appeler les méthodes demandées pour l'élève
eleve1.bonjour()
eleve1.allerEnCours()

# Créer un objet professeur
professeur1 = Professeur("Professeur Arthur", 40)

# Appeler les méthodes demandées pour le professeur
professeur1.bonjour()
professeur1.enseigner()