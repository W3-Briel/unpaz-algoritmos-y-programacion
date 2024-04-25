# alumno: Angel Gabriel Saucedo
# Algoritmos y Programacion - B1

import array as arr
############################ FUNCIONES ############################
# Escriba un programa que utilice tres funciones, que dada una secuencia numérica (lista,
# tupla, vector) debe:
# a. Encontrar el mayor de los valores
# b. Calcular el promedio
# c. Encontrar el valor más bajo
# El programa debe mostrar los tres resultados por pantalla.

# VECTOR POR DEFECTO
vector = arr.array("i",[-1,-2,4,-4,-5,0])

def mayor(lista):
    return print(max(lista))

def menor(lista):
    return print(min(lista))

def promedio(lista):
    acumulador = 0
    for numero in lista:
        acumulador += numero
    return print(acumulador/len(lista))

mayor(vector)
menor(vector)
promedio(vector)

####### metodo alternativo para mayor y menor;

# def mayor_metodo_alternativo(lista):
#     mayor = lista[0]
#     for numero in lista:
#         if mayor < numero: mayor = numero
#     return print(mayor)

# def menor_metodo_alternativo(lista):
#     menor = lista[0]
#     for numero in lista:
#         if menor > numero: menor = numero
#     return print(menor)

# mayor_metodo_alternativo(vector)
# menor_metodo_alternativo(vector)