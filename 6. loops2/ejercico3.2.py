# Escribir un programa que pida al usuario que ingrese
# una contraseña hasta que coincida con una contraseña predefinida

contrasena_predefinida = "HolaProgramadores"

# Número máximo de intentos permitidos
intentos_max = 4

# Contador para la comprobación de intentos
intentos = 0

# Bucle para pedir la contraseña hasta que coincida o se alcancen los intentos máximos
while intentos < intentos_max:
    contrasena = input("Ingrese contraseña: ")
    if contrasena == contrasena_predefinida:
        print("Contraseña correcta.")
        break # Salir del bucle
    else:
        # Incrementar los intentos y mostrar mensaje de error si es necesario
        intentos += 1 
        intentos_restantes = intentos_max - intentos
        if intentos_restantes > 0:
            print(f"Contraseña incorrecta, te quedan {intentos_restantes} intentos")
        else:
            print("Has superado el número máximo de intentos")

