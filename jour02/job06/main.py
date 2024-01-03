class Commande:
    def __init__(self, numero_commande):
        self.__numero_commande = numero_commande
        self.__plats_commandes = {}
        self.__statut_commande = "en cours"

    def ajouter_plat(self, nom_plat, prix_plat):
        if nom_plat not in self.__plats_commandes:
            self.__plats_commandes[nom_plat] = {"prix": prix_plat, "statut": "en cours"}
            print(f"Plat '{nom_plat}' ajouté à la commande.")

    def annuler_commande(self):
        self.__statut_commande = "annulée"
        print("La commande a été annulée.")

    def calculer_total(self):
        total = sum(plat["prix"] for plat in self.__plats_commandes.values() if plat["statut"] == "en cours")
        return total

    def afficher_commande(self):
        print(f"Commande #{self.__numero_commande}:")
        for nom_plat, plat in self.__plats_commandes.items():
            print(f"{nom_plat}: {plat['prix']} $ ({plat['statut']})")
        total = self.calculer_total()
        print(f"Total à payer: {total} $")

    def calculer_tva(self, taux_tva=0.1):
        tva = self.calculer_total() * taux_tva
        return tva


# Exemple d'utilisation de la classe Commande
commande1 = Commande(numero_commande=1)
commande1.ajouter_plat("Pizza", 12.99)
commande1.ajouter_plat("Salade", 8.99)
commande1.afficher_commande()

commande1.annuler_commande()
commande1.afficher_commande()

tva_commande1 = commande1.calculer_tva()
print(f"TVA de la commande: {tva_commande1} $")