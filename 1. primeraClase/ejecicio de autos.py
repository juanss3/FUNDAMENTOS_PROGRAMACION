'''Una compañia de venta de autos usados, paga a su personal de ventas un salario de 
$1000 mensuales, mas una comisión de $150 por cada auto vendido, más el 5% del valor de
la venta por auto. Cada mes el capturista de la empresa ingresa en la computadora los 
datos pertinentes.
Hacer un programa que calcule e imprima el salario mensual de un vendedor '''
#vriables
salarioNeto = 1000
comision = 150
porcentajeValorDeLaVenta = 0.05
ventaCarros = float(input("¿cuantos carros se vendieron?: "))
valorVenta = float(input("valor total de las ventas:  "))

#operaciones
comisionNeto = comision * ventaCarros
ValorTotalVenta = valorVenta * porcentajeValorDeLaVenta
salarioMensual =  comisionNeto + ValorTotalVenta + salarioNeto

#print
print(f"el salario a pagar es: {salarioMensual}")