frutas = ["mora", "lulo", "manzana", "fresa", "maracuya"]
# me muestra el tipo de datos
print(type(frutas))

# mostrar la lista completa
print("La lista de frutas: ", frutas)

# agregar elemento a la lista
frutas.append("kiwi")
print(frutas)

# Acceder a un elemento y mostrarlo
print("Tercera fruta ", frutas[2])

frutas.append("Melon")
print(frutas)

# eliminar la última fruta de la lista
frutas.pop()
print(frutas)

# contar la cantidad
print("cantidad de frutas en la lista ", len(frutas))

# ordenar la lista alfabéticamente
frutas.sort()
print(frutas)

# eliminar un elemento en específico
frutas.remove("mora")
print(frutas)
