# alumno: Angel Gabriel Saucedo
# Algoritmos y Programacion - B1
########################################
from TDA_clase_6 import Lista_ordenada
from random import randint

mi_lista_de_numeros = Lista_ordenada()

#### VARIABLES DE CONTROL

NUMEROS_A_CARGAR = 1000

VALOR_MINIMO_RANDOM = 5
VALOR_MAXIMO_RANDOM = 300

for i in range(NUMEROS_A_CARGAR):
    numero_aleatorio = randint(VALOR_MINIMO_RANDOM,VALOR_MAXIMO_RANDOM)
    mi_lista_de_numeros.agregar(numero_aleatorio)

mi_lista_de_numeros.ver()