def bus_lineal(lista,x):# creamos la funcion bus_lista que contiene lista y x que es el numero que bamos a buscar
    for i in range(len(lista)):#recorre toda la lista
        if lista [i]== x:# pero si un numero del recorrido i es igual a x nos da la posicion en donde esta x 
            return i
    return "dato no encontrado"



lista =[3,5,2,4,6,7,4,3,2,6,8,1,1,4,6,7,3,2,56,7,3,2,56,8,9,9,8,5,4,2,2,3,45,5,6,7,76]

x = 1       #definimos x

resultado = bus_lineal(lista, x)
print(resultado)