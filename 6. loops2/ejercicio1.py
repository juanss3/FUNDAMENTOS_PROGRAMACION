''' hacer un programa que pid un número y lo muestre el programa para cuando se ingrese un número negativo'''

num = float(input("ingrese un número (ingrese un número negativo para parar): "))

while num >= 0:
    print (f"el numero es {num}")
    num = float(input("ingrese otro número: "))
else:
    print("Terminando programa . . . ")