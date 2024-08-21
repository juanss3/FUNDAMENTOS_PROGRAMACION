'''Cree un programa que pida un numero al usuario y los sume.
El programa termina cuando el usurio ingrese un 0'''

suma = 0
num = int(input("ingrese un numero o ingrese 0 para parar: "))

while num != 0:
    suma += num
    num = int(input("ingrese otro numero: "))

print (f"suma de los numeros ingresados es {suma}")

