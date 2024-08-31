import os


productos = [
    {"nombre": "anillo", "precio": 350, "stock": 8},
    {"nombre": "pulsera", "precio": 180, "stock": 25},
    {"nombre": "reloj", "precio": 120, "stock": 12},
    {"nombre": "aretes", "precio": 650, "stock": 7},
    {"nombre": "collar", "precio": 320, "stock": 9},
    {"nombre": "broche", "precio": 170, "stock": 18},
]

carrito = []

def limpiar_terminal():
    if os.name == "nt": os.system("cls")  # Windows
    else:
        os.system("clear")  # Linux


def productos_disponibles():
    for producto in productos:
        nombre = producto["nombre"]
        precio = producto["precio"]
        cantidad = producto["stock"]
        print(f"\nPRODUCTO: {nombre}   PRECIO: ${precio}   CANTIDAD: {cantidad}")

def add_products(nombre, cantidad):
    limpiar_terminal()
    print("\n---- producto agregado-----")
    try:
        producto = next((p for p in productos if p["nombre"] == nombre), None)
        if producto:
            if producto["stock"] >= cantidad:
                item_carrito = next((c for c in carrito if c["nombre"] == nombre), None)
                if item_carrito:
                    item_carrito["stock"] += cantidad
                else:
                    carrito.append({"nombre": nombre, "precio": producto["precio"], "stock": cantidad})
                    producto["stock"] -= cantidad
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
            print(f"\nPRODUCTO: {nombre}   PRECIO: ${precio}   CANTIDAD: {cantidad}   SUBTOTAL: ${subtotal}")
        print("\n------------------------------------------------------------\n")
    else:
        print("\nEl carrito está vacío")

def precio_total():
    total_carrito = sum(productos["precio"] * productos["stock"] for productos in carrito)
    print(f"Precio Total: ${total_carrito}")

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
                limpiar_terminal()
                print("-------- Agregue producto -------")
                nombre = input("nombre de producto: ")
                cantidad = int(input("cantidad de productos: "))
                add_products(nombre, cantidad)

            elif opcion == 3:
                mostrar_carrito()
                precio_total()

            elif opcion == 4:
                if carrito:
                    mostrar_carrito()
                    precio_total()
                    print("\n1. pagar ahora mismo")
                    print("2. modificar el carrito")
                    try:
                        opcion = int(input("elija una opción: "))
                        if opcion == 1:
                            limpiar_terminal()
                            print("-----------Su compra ha sido realizada-----------")
                            mostrar_carrito()
                            precio_total()
                            break
                        else:
                            limpiar_terminal()
                            main()
                    except ValueError:
                        print("*******OPCION INAVLIDA*********")
                        
                else:
                    print("\nNO HAY PRODUCTOS EN EL CARRITO")

            elif opcion == 5:
                print("Saliendo . . .")
                break

            else:
                print("*************opcion no valida*************")
    except ValueError:
        print("\n*** OPCION INVALIDA ***")
        main()

main()
