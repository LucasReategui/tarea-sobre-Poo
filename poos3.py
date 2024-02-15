#creamos una clase  Abstracta "Animal"
class Animal:
    def __init__(self, sonido):
        self.sonido = sonido
# tambien un metodo abstracto hacer sonido y que retornr del atributo del constructor
    def hacer_sonido(self):
        return self.sonido
    
    def mostrar_sonido(self):
        print(f"Este animal hace este sonido: {self.hacer_sonido()})")

class Perro(Animal):
    def __init__(self):
        super().__init__("el perro hace Guau! Guau!..")
        
        

class Gato(Animal):
    def __init__(self):
        super().__init__("el gato hace Miau..!")

# Crear instancias de Perro y Gato
perro = Perro()
gato = Gato()

# Llamar al método hacer_sonido en objetos de ambas clases
print(perro.hacer_sonido())  # Output: Guau!
print(gato.hacer_sonido())  # Output: Miau!
        