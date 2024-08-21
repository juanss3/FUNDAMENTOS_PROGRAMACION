'''hacer una calculadora'''
def calculadora(operador,x,y):
    def sumar (a,b):
        return a + b

    def resta (a,b):
        return a - b

    def multiplicar (a,b):
        return a * b

    def divicion (a,b):
        if b != 0:
            return a / b
        else:
            return "eror no se puede dividir entre 0"

    if operador == "sumar":
        return sumar (x,y)

    elif operador == "resta":
        return resta (x,y)

    elif operador == "multiplicar":
        return multiplicar (x,y)

    elif operador == "divicion":
        return divicion (x,y)

    else:
        print("opcion no valida . . .")     

resultado = calculadora('divicion',10,5)
print('Resultado: ', resultado)