'''Vamos crear un app que permita ingresar una nota y va evaluar
si es aprobado(5 a 7), notable(8 a 9), sobresaliente(10) y todo menor a esto
reprobado'''

nota = 10

if (nota >= 5 and nota <= 7):
    print("Aprobado")
elif (nota >= 8 and nota <= 9):
    print("Aprobado")
elif (nota == 10):
    print("Aprobado")
elif (nota < 5):
    print("Reprobó")
else: 
    print("******ingree un valor correcto******")
