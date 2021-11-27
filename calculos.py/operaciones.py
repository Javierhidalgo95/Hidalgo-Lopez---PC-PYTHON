
# Solucion 10
i = 1
while (i==1): 
   try:
        a = float(input("Introduce el primer número: "))
        b = float(input("Introduce el segundo número: "))
        print(f"El resultado de la suma es: {a+b}") 
   except:
        print("Tipo de dato no valido")
   
   try:
        a = float(input("Introduce el primer número: "))
        b = float(input("Introduce el segundo número: "))
        print(f"El resultado de la resta es: {a-b}")
   except:
        print("Tipo de dato no valido")
   
   try:
        a = float(input("Introduce el primer número: "))
        b = float(input("Introduce el segundo número: "))
        print(f"El resultado de la multiplicacion es: {a*b}")
   except:
        print("Tipo de dato no valido")
  
   try:
        a = float(input("Introduce el primer número: "))
        b = float(input("Introduce el segundo número: "))
        print(f"El resultado de la division es: {a/b}") 
   except:
        print("Tipo de dato no valido")
        print("No es posible dividir enre cero")
men= input(" desea continuar s(si) n (no)")

   