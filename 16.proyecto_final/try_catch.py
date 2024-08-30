def main():
    try:
        num_1 = int(input("imgrese el numero 1: "))
        num_2 = int(input("imgrese el numero 2: "))
        suma = num_1 + num_2

        print(suma)
    except ValueError:
        print("DATO INGRESADO NO VALIDO")
        main()
main()