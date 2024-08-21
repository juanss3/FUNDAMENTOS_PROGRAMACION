'''Escribir un programa que siga pidiendo al usuario que ingrese una contraseña hasta que coincida 
con la contraseña predefinida'''

password = "HolaProgramadores"
intento_comtra = input("Ingrese la contraseña: ")
intentos = 4

while intento_comtra != password:
    intentos -= 1
    if intentos == 0:
        break
    print("contraseña incorrecta, intente de nuevo")
    intento = input ("ingrese contraseña: ")

print("********** contraseña correcta **********")