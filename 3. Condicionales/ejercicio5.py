'''Clasificar a un estudiante según su calificación. 

Condiciones: Si la calificación es 90 o más, el estudiante tiene una "A". Si está 
entre 80 y 89, tiene una "B". Si está entre 70 y 79, tiene una "C". Si está entre 60 y 
69, tiene una "D". Si es menor a 60, tiene una "F". '''

calificaciones = float(input("Cual es su calificación: "))

if calificaciones >= 90 and calificaciones >= 100:
    print("su nota es A")
elif calificaciones >= 80 and calificaciones >= 89:
    print("su nota es B")
elif calificaciones >= 70 and calificaciones >= 79:
    print("su nota es C")
elif calificaciones >= 60 and calificaciones >=69:
    print("su nota es D")
elif calificaciones >= 0 and calificaciones >= 50:
    print("su nota es F")
else: 
    print ("error")