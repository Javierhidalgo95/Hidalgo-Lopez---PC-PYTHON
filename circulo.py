
# Solucion 3

class Circulo:
    # atributos
    def __init__(self, radio):
        # genero las variables del circulo
        self.radio = radio
    # establecemos funcionalidades 
    def area(self):
        from math import pi
        resultado = pi * self.radio ** 2
        return resultado
        
# Mi programa

# Generamos objetos
Circulo1 = Circulo(4)
Circulo1.area()

# creamos un objeto 2
Circulo2 = Circulo(7)
Circulo2.area()

print('Área del circulo 1: %.2f' % Circulo1.area())
print('Área del circulo 2: %.2f' % Circulo2.area())