''' hacer una aplicacion que le pida al usuario n numeros y los almacene en euna lista,
luego que la ordene y la muestre en pantalla'''

lista_numeros=[]
for i in range (8):
    numeros =(input("ingrese 8 numeros: "))
    lista_numeros.append (numeros)


lista_numeros.sort()
print(lista_numeros)