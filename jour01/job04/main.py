class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        return f"Je m'appelle {self.nom} {self.prenom}."

# Instanciation de plusieurs personnes
personne1 = Personne("Doe", "John")
personne2 = Personne("Smith", "Alice")
personne3 = Personne("Dupont", "Pierre")

# Appel à la méthode SePresenter pour vérifier le bon fonctionnement
print(personne1.SePresenter())
print(personne2.SePresenter())
print(personne3.SePresenter())