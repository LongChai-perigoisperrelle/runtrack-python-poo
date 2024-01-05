class Personne:
    def __init__(self, age=14):
        self.age = age

    def afficherAge(self):
        print("Âge de la personne :", self.age)

    def bonjour(self):
        print("Hello")

    def modifierAge(self, nouvel_age):
        self.age = nouvel_age


class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")

    def afficherAge(self):
        print("J'ai", self.age, "ans")


class Professeur(Personne):
    def __init__(self, age=14, matiereEnseignee=""):
        super().__init__(age)
        self.matiereEnseignee = matiereEnseignee

    def enseigner(self):
        print("Le cours va commencer")


# Instanciation d'une Personne avec l'âge par défaut
personne1 = Personne()
personne1.afficherAge()
personne1.bonjour()

# Instanciation d'un Élève
eleve1 = Eleve()
eleve1.afficherAge()

# Instanciation d'un Professeur
professeur1 = Professeur(age=35, matiereEnseignee="Mathématiques")
professeur1.afficherAge()
professeur1.enseigner()