'''Calcular la tarifa de un taxi según la distancia recorrida.
Condiciones: La tarifa es de $5 por el primer kilómetro,
$2 por cada kilómetro adicional hasta 5 km, y $1.5 por cada kilómetro adicional después de 5 km.'''

distancia= float(input("cual fue la distancia recorrida: "))

if distancia <= 1:
    tarifa = 5
elif distancia <= 5:
    tarifa = 5 +(distancia-1)*2
else: 
    tarifa=13+(distancia-5)*1.5
print ("su trifa es: ",tarifa)