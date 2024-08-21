'''crea un progrma que invierta una palbra '''
def invertir_cadena (cadena:str):
    invertida = ""
    for letra in cadena:
        invertida = letra + invertida
    return invertida
print (invertir_cadena("hola"))