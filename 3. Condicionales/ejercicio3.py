'''Comprobar si un año es bisiesto. 
Condiciones: Un año es bisiesto si es divisible por 4, pero no por 100, a menos que 
sea divisible por 400. '''

anio = int(input("ingrese el año: "))

if (anio % 4 == 0 and anio % 100 != 0 ) or(anio % 400 == 0):
    print ("El año es bisiesto")
else:
    print("el año NO es bisiesto")
