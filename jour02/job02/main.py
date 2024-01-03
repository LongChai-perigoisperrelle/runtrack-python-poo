class Livre:
    def __init__(self, titre, auteur, nb_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nb_pages = nb_pages

    # Assesseurs (getters)
    def get_titre(self):
        return self.__titre

    def get_auteur(self):
        return self.__auteur

    def get_nb_pages(self):
        return self.__nb_pages

    # Mutateurs (setters)
    def set_titre(self, titre):
        self.__titre = titre

    def set_auteur(self, auteur):
        self.__auteur = auteur

    def set_nb_pages(self, nb_pages):
        # Vérification que le nombre de pages est un entier positif
        if isinstance(nb_pages, int) and nb_pages > 0:
            self.__nb_pages = nb_pages
        else:
            print("Erreur : Le nombre de pages doit être un nombre entier positif.")

    # Méthode pour afficher les informations du livre
    def afficher_infos(self):
        print(f"Titre : {self.__titre}")
        print(f"Auteur : {self.__auteur}")
        print(f"Nombre de pages : {self.__nb_pages}")

# Création d'un livre avec des valeurs initiales
mon_livre = Livre("Le Petit Prince", "Antoine de Saint-Denis", 100)

# Affichage des informations initiales
mon_livre.afficher_infos()

# Modification des valeurs, y compris une tentative avec un nombre de pages non valide
mon_livre.set_titre("Nouveau Titre")
mon_livre.set_auteur("Nouvel Auteur")
mon_livre.set_nb_pages(150)  # Modification valide
mon_livre.set_nb_pages("non_valide")  # Tentative de modification avec une valeur non valide

# Affichage des nouvelles informations
mon_livre.afficher_infos()