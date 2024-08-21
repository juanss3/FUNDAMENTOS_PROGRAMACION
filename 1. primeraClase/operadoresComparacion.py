num1 = float(input("por favor digite el primer numero: "))
num2 = float(input("por favor digite el segundo numero: "))

mayorq = num1>num2
menorq = num1 < num2
mayorIgual = num1 >= num2
menorigual = num1 <= num2
igualdad = num1 == num2
diferenteq = num1 != num2

print("el numero 1 es mayor que el numero 2 ", mayorq)
print("el numero 1 es menor que el numero 2 ", menorq)
print("el numero 1 es mayor o igual que el numero 2 ", mayorIgual)
print("el numero 1 es mayor o igual que el numero 2 ", menorigual)
print("el numero 1 es igual que el numero 2 ", igualdad)
print("el numero 1 es diferente que el numero 2 ",  diferenteq)