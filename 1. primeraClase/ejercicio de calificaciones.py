'''/*5. La calificación final de un estudiante de Informática se calcula con base a las 
calificaciones de cuatro aspectos de su rendimiento académico: participación, 
primer examen parcial, segundo examen parcial y examen final.
Sabiendo que las calificaciones anteriores entran a la calificación final con 
ponderaciones del 10%, 25%, 25% y 40%, Hacer un programa que calcule e imprima la 
calificación final obtenida por un estudiante.*/'''

participacion = float(input("digite la nota de participacion: "))
primerParcial = float(input("digite la nota del primer parcial: "))
segundoParcial = float(input("digite la nota del segundo parcial: "))
examenFinal= float(input("digite la nota del examen final: "))

participacion *= 0.10
primerParcial *= 0.25
segundoParcial *= 0.25
examenFinal*= 0.40

notaFinal = participacion + primerParcial + segundoParcial + examenFinal

print(f"la nota final es: {notaFinal}")