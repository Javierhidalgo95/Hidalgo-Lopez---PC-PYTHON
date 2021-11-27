
# Solucion 1

def calcular_longitud_cadena(cadena):
    """
    Calcula la longitud de una cadena de caracteres.
    """
    contador = 0

    for c in cadena:
        contador += 1
    
    return contador

texto = 'Amar es compartir'

print(calcular_longitud_cadena(texto))

# Solucion 2

def cambiar_mayusculas(cad):
    return cad
cad = input("Cadena:")				
lista=cad.split(" ")
# Ejemplo, si recibe curso python debe devolver Curso Python
for palabra in lista:
    print (palabra.capitalize(),end=" ")
print()			

# Solucion 7

def triangulo_pascal(filas):
    fila = [1]
    cero = [0]

    for i in range(filas):
        print(fila)

        fila = [i + d for i, d in zip(fila + cero, cero + fila)]


triangulo_pascal(8)