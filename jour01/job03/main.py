class Operation:
    def __init__(self, nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def addition(self):
        resulta = self.nombre1 + self.nombre2
        print("Résulta de l'addition :", resulta)    

# Example d'utilisation
operation_instance = Operation(nombre1=5, nombre2=7)
operation_instance.addition()