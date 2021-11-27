
# Solucion 9

import random

numero = int(input("Introduzca un numero entre el 1 y el 100: "))
aleatorio = random.randint(0,100) 
if numero == aleatorio: 
   print("Has ganado")
else: 
   print("el número aleatorio es superior o inferior al introducido, solicitar un nuevo número")
