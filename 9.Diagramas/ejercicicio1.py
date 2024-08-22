while True:
    a = float(input("Ingrese su primer numero: "))
    b = float(input("Ingrese su segundo numero: "))

    if a == b:
        print ("no valido, deben ser diferentes") 
    else:
        if a > b:
            print("a es mayor")
        else:
            print("b es mayor")
        break

