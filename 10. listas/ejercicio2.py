'''Mini Proyecto: Gestor de Tareas

Objetivo:
Crear una aplicación de consola que permita al usuario gestionar una lista de tareas. 
El usuario podrá añadir tareas, ver la lista de tareas, ordenarlas por prioridad, y eliminar tareas completadas.

Funcionalidades:
Añadir Tarea: Permite al usuario añadir una nueva tarea con una descripción y una prioridad.
Mostrar Tareas: Muestra todas las tareas actuales.
Ordenar Tareas: Ordena las tareas por su prioridad.
Eliminar Tarea: Permite al usuario eliminar una tarea completada.
Estructura del Proyecto:
La lista de tareas será una lista de diccionarios, donde cada diccionario representará una tarea con una descripción 
y una prioridad.'''

tareas = []

def agregar_tarea(tareas):
    print()
    print("-------------------------------AGREGAR TAREA-----------------------------")
    
    descripcion = input("ingrese una descripcion a su tarea: ")
    prioridad = int(input("ingrese una prioridad del 1 al 10: "))
    tarea = {"descripcion":descripcion , "prioridad":prioridad }
    tareas.append(tarea)
    print("**** tarea agregada con exito ****")

def mostrar_tareas(tareas):
    if len (tareas) == 0:
        print()
        print("---no hay tareas---")
    else:
        for i, tarea in enumerate(tareas):
            print()
            print(f"{i+1}. {tarea['descripcion']}- prioridad: {tarea['prioridad']}")


def ordenar_tareas(tareas):
    tareas.sort(key = lambda x: x ["prioridad"])
    print()
    print("-_-_-_-_-_-_-_-_-_- tarea ordenada por prioridad -_-_-_-_-_-_-_-_-_-_-")


def eliminar_tareas(tareas):
    pass


def menu():
    #borrar despues (tareas de prueba)
    tareas = [{"descripcion":"Programar ciclos", "prioridad": 5},

            {"descripcion":"Programar condicinales", "prioridad": 10},

            {"descripcion":"Programar variables", "prioridad": 8}]
    
    while True:
        print()
        print("******* gestion de tareas*******")
        print()
        print("1. agregar tarea")
        print("2. mostrar tarea")
        print("3. ordenar tarea por prioridad")
        print("4. eliminar tarea ")
        print("5. salir")
        opcion = input("elija una opcion: ")
        
        if opcion == "1":
            agregar_tarea(tareas)
        elif opcion == '2':
            mostrar_tareas(tareas)
        elif opcion == '3':
            ordenar_tareas(tareas)
        elif opcion == '4':
            pass
        elif opcion == '5':
            print("Saliendo del programa . . . ")
            break
        else:
            print()
            print("################################### error elija una opcion valida ############################################")
menu ()