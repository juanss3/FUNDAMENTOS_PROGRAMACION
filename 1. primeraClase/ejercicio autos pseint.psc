Algoritmo ejercicioCarros
	definir salarioNeto,comision,porcentajeValorDeLaVenta,valorVenta,comisionNeto,valorTotalVenta,salarioMensual como real
	definir ventaCarros Como Entero
	salarioNeto = 1000
	comision = 150
	porcentajeValorDeLaVenta = 0.05
	
	Escribir "¿Cuantos carros se vendieron?:"
	Leer ventaCarros
	
	Escribir "Valor total de las ventas:"
	Leer valorVenta
	
	comisionNeto = comision * ventaCarros
	valorTotalVenta = valorVenta * porcentajeValorDeLaVenta
	salarioMensual = comisionNeto + valorTotalVenta + salarioNeto
	
	Escribir "el salario a pagar es: " salarioMensual
	
FinAlgoritmo
