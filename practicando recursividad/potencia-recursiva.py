# alumno: Angel Gabriel Saucedo
# Algoritmos y Programacion - B1

######################## FUNCIONES RECURSIVAS #########################
# Implementar una función para calcular la potencia dado dos números enteros, el primero
# representa la base y el segundo el exponente.

def potencia_recursiva(base,exponente):
    if base == 1 or base == 0 or exponente == 1:
        return base
    elif exponente == 0 and base != 0:
        return 1
    else:
        return base * potencia_recursiva(base,exponente-1)

print(potencia_recursiva(2,2))