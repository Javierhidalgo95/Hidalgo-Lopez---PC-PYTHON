
# Solucion 4

class Rectangulo:
     # atributos
    def __init__(self, largo, ancho):
        # genero las variables del rectangulo
        self.largo = largo
        self.ancho = ancho
    # establecemos funcionalidades 
    def area(self):
        resultado = self.ancho * self.largo
        return resultado
    
# Mi programa

# Generamos objetos
Rectangulo1 = Rectangulo(10,5)
Rectangulo1.area()

# creamos un objeto 2
Rectangulo2 = Rectangulo(16,9)
Rectangulo2.area()

print('Área del rectángulo 1: %.2f' % Rectangulo1.area())
print('Área del rectángulo 2: %.2f' % Rectangulo2.area())

