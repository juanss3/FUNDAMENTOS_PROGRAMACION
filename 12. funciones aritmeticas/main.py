import os
# la funcion de este codigo es limpiar la terminal independientemente del sistema operativo del usuario
def limpiar_terminal():
    if os.name == "nt": os.system("cls")#windows
    else: os.system('clear') #linux o mac

input()
limpiar_terminal()