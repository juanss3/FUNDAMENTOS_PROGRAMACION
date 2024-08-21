'''Vamos a crear una app que nos va a preguntar la edad del usuario
En el caso que el usuario sea mayor de edad y cuente con licencia de conducir,
le va a mostrar un mensaje que le informe que puede conducir.
En el caso que sea mayor de edad pero no tenga licencia,
le mostrará que no puede conducir porque no tiene licencia.
En el caso que sea menor de edad, le informará que no puede conducir por este motivo.'''

edad = int(input("¿Cuál es tu edad?: "))
tiene_licencia = (input("¿Tienes licencia de conducir? ingrese: (SI) / (NO): ")).lower()

if edad >= 18:
    if tiene_licencia == "si":
        print("Puedes conducir.")
    else: 
        print("No puedes conducir porque no tienes licencia.")
else:
    print("No puedes conducir porque eres menor de edad.")
