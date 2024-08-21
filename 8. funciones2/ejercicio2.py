'''funciones anidadas para validar y filtrar datos'''
def procesar_numeros(numeros:list):
    def es_positivo (n):
        return n > 0
    
    def sumar_positivos (lista):
        total = 0
        for numero in lista:
            if es_positivo(numero):
                total += numero
        return total
    return sumar_positivos(numeros)

numeros = [4,6,2,3,-7,3,-7,8,-65,6,-312,-7,5,1]
print(f"suma de los numeros positivos: {procesar_numeros(numeros)}")