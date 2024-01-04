class Ville:
    def __init__(self, nom, nombre_habitants):
        self._nom = nom
        self._nombre_habitants = nombre_habitants

    def get_nombre_habitants(self):
        return self._nombre_habitants

    def augmenter_population(self):
        self._nombre_habitants += 1

class Personne:
    def __init__(self, nom, age, ville):
        self._nom = nom
        self._age = age
        self._ville = ville

    def ajouterPopulation(self):
        self._ville.augmenter_population()

# Création d'objets Ville
paris = Ville("Paris", 1000000)
marseille = Ville("Marseille", 861635)

# Affichage du nombre d'habitants des villes
print(f"Nombre d'habitants de {paris._nom}: {paris.get_nombre_habitants()}")
print(f"Nombre d'habitants de {marseille._nom}: {marseille.get_nombre_habitants()}")

# Création d'objets Personne
john = Personne("John", 45, paris)
myrtille = Personne("Myrtille", 4, paris)
chloe = Personne("Chloé", 18, marseille)

# Ajout de population suite à l'arrivée de nouvelles personnes
john.ajouterPopulation()
myrtille.ajouterPopulation()
chloe.ajouterPopulation()

# Affichage du nombre d'habitants après l'arrivée de nouvelles personnes
print(f"Nombre d'habitants de {paris._nom} après l'arrivée de John et Myrtille: {paris.get_nombre_habitants()}")
print(f"Nombre d'habitants de {marseille._nom} après l'arrivée de Chloé: {marseille.get_nombre_habitants()}")