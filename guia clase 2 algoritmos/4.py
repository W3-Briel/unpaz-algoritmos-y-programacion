# alumno: Angel Gabriel Saucedo
# Algoritmos y Programacion - B1

import random as r
import array as arr
############################## ARRAYS ##############################
# Escriba un programa que simule ser un sorteo al azar con 58 participantes. 
# Tenemos sus números de DNI, los participantes tienen números de dni entre 43158258 y 
# 44200952, no puede haber participantes repetidos, una vez cargados los dni, debe seleccionar 
# 3 ganadores al azar, no se pueden repetir los ganadores, 
# muestre el listado de participantes, muestre el número de dni de los ganadores 

# controlador
NUMERO_DE_PARTICIPANTES = 58
NUMERO_INICIAL_DNI = 43158258
NUMERO_TERMINAL_DNI = 44200952

# inicializamos y cargamos los participantes al vector.
participantes = arr.array("i", [])

while len(participantes) < NUMERO_DE_PARTICIPANTES:
    numero_dni_aleatorio = r.randint(NUMERO_INICIAL_DNI,NUMERO_TERMINAL_DNI)
    if numero_dni_aleatorio not in participantes:
        participantes.append(numero_dni_aleatorio)

# ganadores
primero,segundo,tercero = r.sample(participantes, k= 3) # sample es un metodo de la libreria random que elije de forma aleatoria pero se asegura de que no se repitan.

# output
print("PATICIPANTES: \n",*participantes)
print(f"GANADORES: \nprimero {primero}\nsegundo {segundo}\ntercero {tercero}")