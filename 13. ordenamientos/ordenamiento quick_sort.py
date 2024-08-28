
def quick_sort(lista):
    if len(lista)<=1:
        return lista
    else:
        
        pivote = lista[0] #pivote coge siempre el primer numero en la posicion 0 
        menores = [x for x in lista[1:] if x <= pivote] # hace una lista con los menores del pivote 
        mayores = [x for x in lista[1:] if x > pivote]# hace una lista con los mayores del pivote 
        return quick_sort(menores) + [pivote] + quick_sort(mayores)


lista =[3,5,2,4,6,7,4,3,2,6,8,1,1,4,6,7,3,2,56,7,3,2,56,8,9,9,8,5,4,2,2,3,45,5,6,7,7]
lista_ordenada = quick_sort(lista)
print(lista_ordenada)

