Algoritmo sin_titulo
	
	Definir  mayorq, menorq, mayorIgual, menorIgual, igualdad, diferenteq Como Logico
	definir num1, num2 Como Real
	
	Escribir "por favor digite el primer numero"
	leer num1
	Escribir "por favor digite el segundo numero"
	leer num2
	
	mayorq = num1 > num2
	menorq = num1 < num2
	mayorIgual = num1 >= num2
	menorigual = num1 <= num2
	igualdad = num1 = num2
	diferenteq = num1 <> num2
	
	Escribir "el numero 1 es mayor que el numero 2 ", mayorq
	Escribir "el numero 1 es menor que el numero 2 ", menorq
	Escribir "el numero 1 es mayor o igual que el numero 2 ", mayorIgual
	Escribir "el numero 1 es mayor o igual que el numero 2 ", menorigual
	Escribir "el numero 1 es igual que el numero 2 ", igualdad
	Escribir "el numero 1 es diferente que el numero 2 ",  diferenteq
	
FinAlgoritmo
