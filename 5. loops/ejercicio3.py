'''contar cuantas vocales hay en una palabra escrita por el usuario'''

palabra = input("ingrese una palabra: ").lower()

vocales = "aeiou"
contador = 0
numeros = "1234567890"
tiene_numeros= False

for letra in palabra:
    
    if letra in numeros:
        tiene_numeros = True
        break
        
    if letra in vocales:
        contador = contador + 1 #tambien "contador += 1
if tiene_numeros:
    print("error")
else:
    print(f"el numero de vocales en la palabra {palabra} es {contador}")
