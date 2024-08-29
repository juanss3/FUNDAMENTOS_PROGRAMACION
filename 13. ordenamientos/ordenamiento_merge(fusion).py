


def merge_sort(lista):
    if len(lista) > 1:
        mitad = len(lista) // 2
        
        izq = lista[:mitad]
        der = lista [mitad:]
        
        merge_sort(izq)
        merge_sort(der) #parte la lista de mitad en mitad
        
        i = j = k = 0
        
        while i < len(izq) and j < len(der):
            if izq [i]< der[j]:
                lista[k] = izq[i]
                i += 1
            else:
                lista[k]=der[j]
                j += 1
            k += 1
            
        while i < len(izq):
            lista[k]= izq[i]
            i += 1
            k += 1
        while j < len(der):
            lista[k] = der[j]
            j += 1
            k += 1


lista =[3,5,2,4,6,7,4,3,2,6,8,1,1,4,6,7,3,2,56,7,3,2,56,8,9,9,8,5,4,2,2,3,45,5,6,7,7]
merge_sort(lista)
print(lista)

