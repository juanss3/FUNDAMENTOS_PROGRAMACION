
# ordenamiento burbuja

def burbuja(lista):
    n= len(lista) # obtener el tamaño de la lista
    
    for i in range(n):# recorre la lista y guerda el numero del recorrido

        for j in range(0, n-i-1): # en cada recorrido resta 1 numero de la lista para que en ese espacio quede gusradado el numero mayor 

            if lista[j] > lista[j+1]:
                lista[j], lista [j+1] = lista [j+1], lista[j] #con este code se asegua de coger el numero mas graned y posicionaelo en la ultima posición

lista =[3,5,2,4,6,7,4,3,2,6,8,1,1,4,6,7,3,2,56,7,3,2,56,8,9,9,8,5,4,2,2,3,45,5,6,7,76]
burbuja(lista)
print(f"lista ordenada con el metodo burbuja {lista}")
