'''hacer un programa que utilice el ordenamiento de numeros(utilizando el ordenamiento de  mayor a menor)'''
while True:
    a = int(input("ingrese su primer numero: "))
    b = int(input("ingrese su segundo numero: "))
    c = 0
    if a == b:
        print("intente con otros numeros")
    else:
        if a < b:
            c = b
            b = a
            a = c
            
            print(a,b)
        else:
            print("numeros ya ordenados de mayor a menor")
