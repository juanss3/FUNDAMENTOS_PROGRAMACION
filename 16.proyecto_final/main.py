import os
productos = [
    {"nombre": "anillo", "precio": 300, "stock": 10},
    {"nombre": "pulcera", "precio": 150, "stock": 20},
    {"nombre": "reloj", "precio": 100, "stock": 15},
    {"nombre": "aretes", "precio": 600, "stock": 5},
]

def limpiar_terminal():
    if os.name == "nt": os.system("cls")#windows
    else: os.system('clear') #linux o mac

carrito = []

def productos_disponibles():
    for producto in productos:
        nombre = producto["nombre"] 
        precio = producto["precio"]
        cantidad = producto["stock"]
        
        
        print()

        print(f"PRODUCTO: {nombre}   PRECIO: ${precio}   CANTIDAD: {cantidad}")



def add_products(nombre, cantidad):
    limpiar_terminal()
    print()
    print("---- producto agregado-----")
    try:
        producto = next((p for p in productos if p ["nombre"] == nombre), None) #codigo optimizado
        
        if producto:
            if producto ["stock"] >= cantidad:
                
                item_carrito = next((c for c in carrito if c ["nombre"] == nombre),None)
                
                if item_carrito:
                    item_carrito ["stock"] += cantidad
                else:
                    carrito.append({"nombre": nombre,"precio":producto ["precio"],  "stock": cantidad})# append sirve para añadir una lista en la variable carrito
                    producto ["stock"] -= cantidad
            else:
                print(f"no hay suficiente stock para el producto {nombre}")
        else:
            print(f"el producto {nombre} no existe")
    except ValueError:
        print("*** OPCION INVALIDA ***")



def mostrar_carrito():
    print("----------------------- Carrito ------------------------------")
    if carrito:
        for producto in carrito:
            nombre = producto["nombre"]
            precio = producto["precio"]
            cantidad = producto["stock"]
            subtotal = precio * cantidad
            
            print()
            print(f"PRODUCTO: {nombre}   PRECIO: ${precio}   CANTIDAD: {cantidad}   SUBTOTAL: ${subtotal}")
    else:
        print()
        print("El carrito está vacío")


def precio_total(): ##################################################################################
    total_carrito = sum(productos["precio"] * productos["stock"]for productos in carrito)
    
    print(f"el valor del carrito es: $({total_carrito})")


def main():
    try:
        while True:
            
                print("----------Opciones-----------") 
                print("1. mostrar productos")
                print("2. agregar producto al carrito")
                print("3. mostrar carrito")
                print("4. finalizar compra")
                print("5. salir")
            
                opcion = int(input("ingrese una opcion: "))
                if opcion == 1:
                    limpiar_terminal()
                    print("-------- Productos Disponibles -------")
                    productos_disponibles()
                    
                    
                elif opcion == 2:
                    print("-------- Agregue producto -------")
                    nombre = input("nombre de producto: ")
                    cantidad = int(input("cantidad de productos: "))
                    add_products(nombre,cantidad)
                    
                elif opcion == 3:
                    mostrar_carrito()
                    precio_total()
                    
                elif opcion == 4:
                    print()
                    mostrar_carrito()
                    print()# ################################################# terminar ############################
                    print("para pagar pulse 1")
                    
                    break
                elif opcion == 5:
                    print("Saliendo . . .")
                    break
                else:
                    print("*************opcion no valida*************")
    except ValueError:
        print()
        print("*** OPCION INVALIDA ***")
        print()
        main()
    

main()