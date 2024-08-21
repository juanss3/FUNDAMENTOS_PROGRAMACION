num1 = float(input("ingrese el primer numero: "))
num2 = float(input("ingrese el segudo numero: "))
num3 = float(input("ingrese el primer numero: "))

todosPositivos = (num1 > 0) and (num2 > 0 ) and (num3 > 0)
almenosUnPositivo = (num1>0) or (num2 > 0 ) or (num3 > 0)
ningunoPositivo = not(almenosUnPositivo)

print("todos los numeros son positivos: ", todosPositivos)
print("almenos uno es positivo: ", almenosUnPositivo)
print("ninguno es posivo: ", ningunoPositivo)
