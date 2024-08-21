Algoritmo sin_titulo
	definir num1, num2, num3 Como Real
	definir todosPositivos, almenosUnPositivo, ningunoPositivo Como Logico
	
	Escribir "ingrese el primer numero: "
	leer num1
	Escribir "ingrese el segundo numero: "
	Leer num2 
	Escribir "ingrese el tercer numero: "
	Leer num3 
	
	todosPositivos = (num1 > 0) y (num2 > 0 ) y (num3 > 0)
	almenosUnPositivo = (num1>0) o (num2 > 0 ) o (num3 > 0)
	ningunoPositivo = no(almenosUnPositivo)
	
	Escribir "todos los numeros son positivos: ", todosPositivos
	Escribir "almenos uno es positivo: ", almenosUnPositivo
	Escribir "ninguno es posivo: ", ningunoPositivo
FinAlgoritmo

