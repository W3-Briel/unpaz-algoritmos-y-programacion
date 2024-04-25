# alumno: Angel Gabriel Saucedo
# Algoritmos y Programacion - B1

import random as r
import array as arr
############################## ARRAYS ##############################
# Escriba un programa que contenga un vector de 10 posiciones con valores enteros mayores a 
# 1000 y menores a 2000, luego muestre los valores y sus posiciones.

# inicializamos el vector y lo cargamos.
vector = arr.array("i",[])

while len(vector) < 10:
    numero_aleatorio = r.randint(1001,1999)
    vector.append(numero_aleatorio)

# output
for indice,numero in enumerate(vector):
    print(f"pocision: {indice} valor: {numero}")