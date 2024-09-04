# Lista de libros en la biblioteca (predefinidos)
libros = [
    {
        "titulo": "Cien Años de Soledad",
        "autor": "Gabriel García Márquez",
        "isbn": "978-3-16-148410-0",
        "genero": "Ficción",
        "cantidad": 5
    },
    {
        "titulo": "Don Quijote de la Mancha",
        "autor": "Miguel de Cervantes",
        "isbn": "978-1-23-456789-7",
        "genero": "Clásico",
        "cantidad": 3
    },
    {
        "titulo": "La Odisea",
        "autor": "Homero",
        "isbn": "978-0-12-345678-9",
        "genero": "Épico",
        "cantidad": 4
    }
]

usuarios = []

def limpiar_terminal():
    if os.name == "nt": os.system("cls")  # Windows
    else:
        os.system("clear")  # Linux

#funciones de los libros

def agregar_libros():
    print("\n---------- AGREGAR LIBRO ----------\n")
    titulo = input("ingrese el titulo: ")
    autor = input("ingrese el autor: ")
    isbn = input("ingrese el ISBN: ")
    genero = input("ingrese el genero: ")
    cantidad = input("ingrese la cantidad: ")

    nuevo_libro= {
        "titulo" : titulo,
        "autor"  : autor,
        "isbn"  : isbn,
        "genero" : genero,
        "cantidad": cantidad
    }
    libros.append (nuevo_libro)
    print(f"El libro {titulo} ha sido agregado")


def editar_libro():
    print("----- editar libro ----- ")
    
    mostrar_libro()
    
    isbn = input("ingrese el ISBN del libro que quiere editar: ")
    for libro in libros:
        if libro["isbn"] == isbn:
            libro['titulo'] = input(f"Ingrese el nuevo titulo({libro['titulo']}): ")
            libro['autor'] = input(f"Ingrese el nuevo autor({libro['autor']}): ")
            libro['genero'] = input(f"Ingrese el nuevo genero({libro['genero']}): ")
            libro['cantidad'] = int(input(f"Ingrese el nueva cantidad({libro['cantidad']}): "))
            print(f"El libro con el ISBN: {isbn} ha sido actulizado")
            print(f"{libro["titulo"]} - {libro["autor"]} - ISBN: {libro["isbn"]} - {libro["genero"]} - {libro["cantidad"]}")


def eliminar_libro():
    print("---------- Elimiando libro ----------")
    mostrar_libro()
    isbn = input("Ingrese el ISBN del libro que desea eliminar: ")
    global libros
    libros = [libro for libro in libros if libro['isbn'] != isbn]
    print(f"El libro con el ISBN: {isbn} ha sido eliminado")


def mostrar_libro():
    if libros:
        print("lista de libros en la biblioteca")
        for libro in libros:
            print(f"\n --> {libro["titulo"]} / {libro["autor"]} / ISBN: {libro["isbn"]} / {libro["genero"]} / Cantidad: {libro["cantidad"]}")
    else:
        print("No hay libros")


# funciones de usuarios

def agregar_usuario():
    print("\n---------- AGREGAR USUARIO ----------\n")
    nombre = input("ingrese el nombre de usuario: ")
    usuario_id= input("ingrese el id del usuario: ")


    nuevo_usuario= {
        "nombre" : nombre,
        "usuario_id"  : usuario_id,

    }
    usuarios.append (nuevo_usuario)
    print(f"El usuario {nombre} ha sido agregado")


def editar_usuario():
    print("----- editar usuario ----- ")
    
    mostrar_usuario()
    
    usuario_id = input("ingrese el id del usuario que quiere editar: ")
    for usuario in usuarios:
        if usuario["usuario_id"] == usuario_id:
            usuario['nombre'] = input(f"Ingrese el nuevo nombre de usuario({usuario['nombre']}): ")
            usuario['usuario_id'] = input(f"Ingrese el nuevo id de usuario({usuario['usuario_id']}): ")
            
            print(f"El usuario con el id: {usuario_id} ha sido actulizado")
            print(f"{usuario["nombre"]} - {usuario["usuario_id"]} ")


def eliminar_usuario():
    print("---------- Eliminando usuario ----------")
    mostrar_usuario
    usuario_id = input("Ingrese el id del usuario que desea eliminar: ")
    global usuarios
    usuarios = [usuario for usuario in usuarios if usuario['usuario_id'] != usuario_id]
    print(f"El usuario con el id: {usuario_id} ha sido eliminado")


def mostrar_usuario():
    if usuarios:
        print("lista de usuarios registrados en la biblioteca")
        for usuario in usuarios:
            print(f"\n --> {usuario["nombre"]} / {usuario["usuario_id"]} ")
    else:
        print("No hay usuarios")


#funciones de prestamos y devoluciones
def prestamo_libros():
    pass

def devolucion_libros():
    pass

def informe_prestamos():
    pass



# funcion principal del menu
def menu():
    while True:
        print("----- Menu -----")
        print("1. Agregar libro")
        print("2. Editar libro")
        print("3. Eliminar libro")
        print("4. Agregar usuario")
        print("5. Editar usuario")
        print("6. Eliminar usuario")

        print("0. Finalizar")

        opcion = int(input("Selecciona una opcion: "))

        if opcion == 1:
            agregar_libros()
        elif opcion == 2:
            editar_libro()
        elif opcion == 3:
            eliminar_libro()
        elif opcion == 4:
            agregar_usuario()
        elif opcion == 5:
            editar_usuario()
        elif opcion == 6:
            eliminar_usuario()
        elif opcion == 0:
            break

menu()

