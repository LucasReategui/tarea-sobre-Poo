#Creando Clase base forma
class Forma:
    def __init__(self):
        pass #se utiliza como un marcador de posición en el código
#creamos su metodo dibujar()
    def dibujar(self):
        print("Dibujando forma")

#Creamos otra clase base color
class Color:
    def __init__(self, color):
        self.color = color

    def pintar(self):
        print(f"Pintando con {self.color}")

#Creamos una clase que herede ambas clases
class CuadradoColorido(Forma, Color):
    def __init__(self, color):
        Forma.__init__(self)
        Color.__init__(self, color)
# utilizamos super() para llamar  a los metodos de las
#clases padres en el constructor y en  la sobrecarga del método
    def dibujar(self):
        super().dibujar()
        print("Dibujando un cuadrado")

    def pintar(self):
        super().pintar()
        print("Pintando el cuadrado")


cuadrado = CuadradoColorido("rojo")
cuadrado.dibujar()
cuadrado.pintar()
    

        
