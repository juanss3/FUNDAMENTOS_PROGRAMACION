colores = {
    "red": "rojo",
    "blue": "azul",
    "white": "blanco",
    "yellow": "amarillo"
}

#tipo de dato
print(type(colores))
# ver los valores del diccionario
print(colores)

#Acceder al valor de una clave
print("El color blue en español es ", colores["blue"])
print("El color yellow en español es ", colores["yellow"])

#agregar un elemento al diccionario
colores["black"] = "negro"
print(colores)
colores["green"] = "zapote"
print(colores)

#actualizar el valor clave en un diccionario
colores["green"] = "verde"
print(colores)
del colores["red"]
print(colores)

existeColor = "pink" in colores
print("¿La clave pink está en el diccionario? ", existeColor)

existeColor2 = "black" in colores
print("¿La clave black está en el diccionario? ", existeColor2)

print("cantidad de colores en el diccionario", len(colores))