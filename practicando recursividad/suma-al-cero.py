# alumno: Angel Gabriel Saucedo
# Algoritmos y Programacion - B1

######################## FUNCIONES RECURSIVAS #########################
# Implementar una función que calcule la suma de todos los números enteros comprendidos
# entre cero y un número entero positivo dado.

# funcion recursiva
def suma_recursiva_al_cero(numero_positivo):
    if numero_positivo == 0:
        return 0
    return numero_positivo + suma_recursiva_al_cero(numero_positivo-1)

#input - excepciones
while True:
    try:
        numero_positivo = int(input("ingresa un numero positivo: "))
    except ValueError:
        print("solo numeros!!, intenta denuevo"); continue
    if numero_positivo >= 0: break
    else: print("SOLO NUMEROS POSITIVOS!")

#output
print("la suma de todos los numeros entre cero y el numero dado, es; ",suma_recursiva_al_cero(numero_positivo))