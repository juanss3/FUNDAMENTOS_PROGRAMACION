'''hacer una calculadora'''

def suma (x,y):
    return x + y

def resta (x,y):
    return x - y

def producto (x,y):
    return x * y

def divicion (x,y):
    if y != 0:
        return x / y
    else:
        return "eror no se puede dividir entre 0"

def opciones ():
    print("opciones: ")
    print("1. SUMA ")
    print("2. RESTA ")
    print("3. MULTIPLICAR ")
    print("4. DIVIDIR ")
    print ("5. SALIR")

def calculadora():
    opciones()
    while True:
        operacion = int (input("ingrese la opcion que desea: "))
        if (operacion >=1 and operacion <= 5):
            if operacion == 1:
                num1 = float(input("ingrese el primer numero: "))
                num2 = float(input("ingrese el segundo numero: "))
                
                print ("el resultado es: ", suma(num1,num2))
                print ("################################################")
                print ()
                opciones()
                
            elif operacion == 2:
                num1 = float(input("ingrese el primer numero: "))
                num2 = float(input("ingrese el segundo numero: "))
                
                print ("el resultado es: ", resta(num1,num2))
                print ("################################################")
                print ()
                opciones()
            elif operacion == 3:
                num1 = float(input("ingrese el primer numero: "))
                num2 = float(input("ingrese el segundo numero: "))
                
                print ("el resultado es: ", producto(num1,num2))
                print ("################################################")
                print ()
                opciones()
            elif operacion == 4:
                num1 = float(input("ingrese el primer numero: "))
                num2 = float(input("ingrese el segundo numero: "))
                
                print ("el resultado es: ", divicion(num1,num2))
                print ("################################################")
                print ()
                opciones()
            elif operacion == 5:
                print("saliendo . . . ")
        else:
                print("opcion no valida . . .")     
                print("#################################################")
                print()
                opciones()
calculadora()