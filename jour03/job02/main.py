class CompteBancaire:
    def __init__(self, numero_compte, nom, prenom, solde, decouvert=False):
        self.__numero_compte = numero_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert

    def afficher(self):
        print(f"Numéro de compte : {self.__numero_compte}")
        print(f"Nom : {self.__nom}")
        print(f"Prénom : {self.__prenom}")
        print(f"Solde : {self.__solde} €")
        print(f"Découvert autorisé : {'Oui' if self.__decouvert else 'Non'}")

    def afficherSolde(self):
        print(f"Solde actuel : {self.__solde} €")

    def versement(self, montant):
        self.__solde += montant
        print(f"Versement de {montant} € effectué. Nouveau solde : {self.__solde} €")

    def retrait(self, montant):
        if self.__solde - montant >= 0 or self.__decouvert:
            self.__solde -= montant
            print(f"Retrait de {montant} € effectué. Nouveau solde : {self.__solde} €")
        else:
            print("Solde insuffisant. Opération impossible.")

    def agios(self, taux_agios):
        if self.__solde < 0:
            agios = abs(self.__solde) * taux_agios
            self.__solde -= agios
            print(f"Agios appliqués : {agios} €. Nouveau solde : {self.__solde} €")
        else:
            print("Pas d'agios à appliquer.")

    def virement(self, compte_destinataire, montant):
        if self.__solde - montant >= 0 or self.__decouvert:
            self.__solde -= montant
            compte_destinataire.versement(montant)
            print(f"Virement de {montant} € effectué vers le compte {compte_destinataire.__numero_compte}.")
        else:
            print("Solde insuffisant. Virement impossible.")


# Création d'un compte
compte1 = CompteBancaire(numero_compte="123456", nom="Dupont", prenom="Jean", solde=1000)

# Test des méthodes
compte1.afficher()
compte1.afficherSolde()
compte1.versement(500)
compte1.retrait(200)
compte1.agios(taux_agios=0.05)

# Création d'un compte à découvert
compte2 = CompteBancaire(numero_compte="789012", nom="Martin", prenom="Sophie", solde=-200, decouvert=True)

# Virement du compte1 vers le compte2
compte1.virement(compte_destinataire=compte2, montant=300)

# Affichage des comptes après le virement
print("\nAprès le virement :")
compte1.afficher()
compte2.afficher()