def funcion_externa(mensaje):
    print(f"mensaje desde la funcion externa: {mensaje}")
    
    def funcion_interna():
        print(f"mensaje desde la funcion interna: {mensaje}")
    
    funcion_interna()
funcion_externa("hola")