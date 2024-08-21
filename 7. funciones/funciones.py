# función simple 
print()
print("**funcion simple**")
print()
def saludar ():
    print("hola")

saludar()

# función con parametros
print()
print("**función con parametros**")
print()
def saludar2(nombre: str):
    print(f"hola {nombre} bienvenido")

saludar2("juan")
saludar2("diego")
saludar2("nicolas")
saludar2("david")

# función con valores de retorno
print()
print("**función con valores de retorno**")
print()
def suma (numero1:float, numero2:float):
    return numero1 + numero2
resultado = suma (3,4)
print(resultado)