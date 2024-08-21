'''Escribe una función llamada es_par que reciba número
y devuelva si es par o no'''

def es_par(numero):
    return numero % 2 == 0

numero = int(input("ingrese un numero: "))
validacion = es_par (numero)
print(validacion)