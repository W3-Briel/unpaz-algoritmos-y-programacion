# alumno: Angel Gabriel Saucedo
# Algoritmos y Programacion - B1

############################ FUNCIONES ############################
# Desarrollar una función que reciba un string como parámetro y nos muestre la cantidad de
# vocales. Llamarla desde el bloque principal del programa 3 veces con string distintos
# ingresados por teclado.

def contador_de_vocales(palabras):
    vocales = ("a","e","i","o","u")
    vocales_en_palabras = 0
    for letra in palabras:
        if letra in vocales: vocales_en_palabras += 1

    return print(f"se encontraron: {vocales_en_palabras} vocales.")

for i in range(3):
    palabras = input("contar vocales de: ").lower()
    contador_de_vocales(palabras)