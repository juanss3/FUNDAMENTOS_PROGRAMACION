'''crear un programa que defina un numero del 1 al 100 y el jugardor debe de adivinar el numero
y el programa le indicara si esta caliente o frio'''
import random


numero_win = random.randint(1,100)
print ("adivine el numero entre el 1 al 100")
intento = int(input("ingrese su intento: "))


while intento != numero_win:
    if intento > numero_win:
        diferencia = intento - numero_win
    else:
        diferencia = numero_win - intento
    
    if diferencia <= 10:
        print("estas hot ;) ")
    else:
        print("estas frio :'C ") 
    
    if intento < numero_win:
        print("*** El numero secreto es MAYOR ***")
    
    else:
        print("*** El numero secreto es MENOR ***")
    
    intento = int(input("número equivocado, ingrese otro: "))

print("************************************************************  GANASTE  *************************************************************")