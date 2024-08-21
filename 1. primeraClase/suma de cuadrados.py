'''Hacer un programa que calcule el cuadrado de una suma.
    (a+b)^2 = a^2 + b^2 + 2ab'''
    
import math    
    
a = float(input("ingrese el valor de a: "))
b = float(input("ingrese el valor de b: "))

resultado = math.pow(a, 2) + math.pow(b,2) + (2 * a * b )

print(f"el resultado es: {resultado}")

