'''Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:

Menos de 100000 COP 5%

Entre 100000 COP y 200000 COP 15%

Entre 200000 COP y 350000 COP 20%

Entre 350000 COP y 600000 COP 30%

Más de 600000 COP.  45%'''


declaracion_renta = (int(input("ingrese su salario: ")))
impuesto = 0
if declaracion_renta >=1:
    
    if 1 >= declaracion_renta < 100000:
        impuesto = declaracion_renta * 0.05
    
    elif 100000 >= declaracion_renta < 200000:
        impuesto = declaracion_renta * 0.15
    
    elif 200000 >= declaracion_renta < 350000:
        impuesto = declaracion_renta * 0.20
    
    elif 350000 >= declaracion_renta < 600000:
        impuesto = declaracion_renta * 0.30
    else:
        impuesto = declaracion_renta * 0.45
    print (f" su impuesto es de: {impuesto}")
    
else: 
    print("***ingrese un valor valido***")


#otra maneja de hacer el print: print (" su impuesto es de: ",impuesto,)