class Operation:
    def __init__(self, nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

# Créez une instance de la classe Operation avec des valeurs spécifiques
operation_instance = Operation(nombre1=12, nombre2=3)

# Imprimez les valeurs des attributs "nombre1" et "nombre2"
print("Valeur de nombre1:", operation_instance.nombre1)
print("Valeur de nombre2:", operation_instance.nombre2)