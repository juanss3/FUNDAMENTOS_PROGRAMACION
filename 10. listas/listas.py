mi_lista = [10, "hola", 3.14, True]

#acceder a todos elemento
print (mi_lista)

nombres = []

#agregar elementos a la lista (.append)
nombres.append("Juan")
nombres. append("Manuel")
#print(nombres)

# acceder a datos con negativos
# accede al dato de adelante hacia atras diferente a de atras a adelante como es normal
#print(mi_lista[-1])

#modificar datos
mi_lista[3]= "zapato"
#print(mi_lista)

#insertar datos
#inserta un dato en la posicion asignada y corre el resto no los elimina 
mi_lista.insert(2,"ola")
#print(mi_lista)

#eliminar dato
#este elimina solo el primero que encuentre si hay datos repetidos 
nombres.insert (1,"Juan")
#print(nombres)
nombres.remove('Juan')
#print(nombres)

# recorrer lista

#for datos in mi_lista:
    #print(datos)


#ordenar lista

numeros = [1,2,3,4,23,3,12,2,5,6,722,5,78,8,9,2,3,45,1,2,6,3,7,5,4,3,24,4,4,4,4,4,4,3]
#print(numeros, "sin ordenar")

# menor a mayor
numeros.sort()
#print(numeros, 'ordenados de menor a mayor')

#mayor a menor 
numeros.sort(reverse=True)
#print(numeros, 'ordenados de mayor a menor')

##########
# ordenar nombres
ejemplo = ["Genesis", "Mancer", "Alchemy", "Flow", "Script", "Forge", "Wave", "Nest", "Whisper", "Crafter"]
#print(ejemplo, "sin ordenar")

# A a Z
ejemplo.sort()
#print(ejemplo, 'ordenados de A a Z')

# Z a A
ejemplo.sort(reverse=True)
#print(ejemplo, 'ordenados de Z a l')
len (mi_lista)