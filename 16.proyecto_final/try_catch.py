def evaluar(edad):
    if edad < 18:
        return "menor"
    elif edad > 65:
        return " mayor"
    else:
        return "adulto"

edad = 34

evaluar(edad)