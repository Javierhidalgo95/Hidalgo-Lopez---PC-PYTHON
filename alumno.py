
# Solucion 5

class Alumno:
    # atributos
    def __init__(self, nombre, numero_registro, edad, nota):
        # genero las variables del alumno
        self.nombre = nombre
        self.numero_registro = numero_registro
        self.edad = edad
        self.nota = nota
        
    # establecemos funcionalidades 
    def display(self):
        return '------------ Display ------------\nNombre: {}\nNumero de registro: {}'.format(self.nombre, self.numero_registro)
       
    def setage(self):
        return '\n------------ SetAge ------------\nEdad: {}'.format(self.edad)

    def setnota(self):
        return '\n------------ SetNota ------------\nNota: {}'.format(self.nota)

# Mi programa

# Generamos objetos
Alumno1 = Alumno('Juan', '21348791', '21', "18")
Alumno1.display()
Alumno1.setage()
Alumno1.setnota()
# creamos un objeto 2
Alumno2 = Alumno('Pedro', '21763498', '25', "20")
Alumno2.display()
Alumno2.setage()
Alumno2.setnota()



print(Alumno1.display(),Alumno1.setage(),Alumno1.setnota())
print(Alumno2.display(),Alumno2.setage(),Alumno2.setnota())
