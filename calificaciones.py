
# Solucion 6

while(True):
    try:
        x = input('Escriba varios números separados por coma: ')
        print(x)
        numeros = x.split(',')
        y = numeros
        print("{}/{} = {}".format(x,y,x/y))
    except:
        print("Ha ocurrido un error, introduce bien el número")
    else:
        print("Todo ha funcionado correctamente")
