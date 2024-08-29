import os
productos = [
    {"nombre": "laptop", "precio": 3000000.00, "stock": 10},
    {"nombre": "mouse", "precio": 150000.00, "stock": 20},
    {"nombre": "teclado", "precio": 100000.00, "stock": 15},
    {"nombre": "monitor", "precio": 600000.00, "stock": 5},
]

def limpiar_terminal():
    if os.name == "nt": os.system("cls")#windows
    else: os.system('clear') #linux o mac
    
carrito = []

def add_products(nombre, cantidad):
    limpiar_terminal()
    print()
    print("----------------------- añadir productos------------------------------")
    producto = next((p for p in productos if p ["nombre"] == nombre), None) #codigo optimizado
    
    if producto:
        if producto ["stock"] >= cantidad:
            
            item_carrito = next((c for c in carrito if c ["nombre"] == nombre),None)
            
            if item_carrito:
                item_carrito ["stock"] += cantidad
            else:
                carrito.append({"nombre": nombre,  "stock": cantidad})# append sirve para añadir una lista en la variable carrito
                producto ["stock"] -= cantidad
        else:
            print(f"no hay sufucunete stock para el producto {nombre}")
    else:
        print(f"el producto {nombre} no existe")
            
            
    print(carrito)
    
    
    
    
def delete_products():
    pass

def delete_cart():
    pass

def buy_products():
    pass

def main():
    while True:
        print("----------Opciones-----------") 
        print("1. añadir producto")
        print("2. quitar producto")
        print("3. borrar carrito")
        print("4. comprar producto")
        print("5. salir")
        
        opcion = int(input("ingrese una opcion: "))
        
        if opcion == 1:
            limpiar_terminal()
            print("-------- agregue producto -------")
            nombre = input("nombre de producto: ")
            cantidad = int(input("cantidad de productos: "))
            add_products(nombre,cantidad)
        elif opcion == 2:
            pass
        elif opcion == 3:
            pass
        elif opcion == 4:
            pass
        elif opcion == 5:
            print("Saliendo . . .")
        else:
            print("*************opcion no valida*************")
        
main()