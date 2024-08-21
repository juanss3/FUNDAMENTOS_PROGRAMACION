'''Vamos a crear programa que simule el juego de Adivinar'''

import random

#Lista de palabras para el juegos
palabras = ['python','scrum','programacion','metodologia']

def elegir_palabra(palabras:list):
    #Elegimos la palabra
    return random.choice(palabras)

def juagar_adivinar_palabra (palabra):
    intentos = 3 
    
    print("Bienvenidos al juego de adivinar la palabra")
    print(f"tiene {intentos} para adivinar la palabra")
    
    while intentos > 0:
        intento = input("adivina la palabra: ").lower() 
        
        if intento == palabra:
            print("FELICIDADES GANASTE")
            break
        else:
            intentos -= 1
            if intentos > 0:
                print(f"aun te quedan {intentos}")
            else: 
                print("ya no hay intentos")
                print(f"la palabra era: {palabra}")
    
palabra = elegir_palabra(palabras)

juagar_adivinar_palabra(palabra)
