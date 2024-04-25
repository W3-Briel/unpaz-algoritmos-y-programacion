# alumno: Angel Gabriel Saucedo
# Algoritmos y Programacion - B1
########################################
from TDA_clase_6 import Lista_no_ordenada
from random import randint

#creamos instanciamos 3 listas no ordenadas, distintas.

lista_no_ordenada_colores = Lista_no_ordenada()
lista_no_ordenada_nombres = Lista_no_ordenada()
lista_no_ordenada_numeros = Lista_no_ordenada()


### cargamos datos
lista_no_ordenada_colores.agregar("Rosado")
lista_no_ordenada_colores.agregar("Gris")
lista_no_ordenada_colores.agregar("Rojo")
lista_no_ordenada_colores.agregar("Azul")
lista_no_ordenada_colores.agregar("Verde")

lista_no_ordenada_nombres.agregar("Angel")
lista_no_ordenada_nombres.agregar("Agustin")
lista_no_ordenada_nombres.agregar("Alvaro")
lista_no_ordenada_nombres.agregar("Ailin")
lista_no_ordenada_nombres.agregar("Jazmin")

for i in range(5):
    numero_aleatorio = randint(1990,2045)
    lista_no_ordenada_numeros.agregar(numero_aleatorio)

### mostramos las listas

lista_no_ordenada_colores.ver()
lista_no_ordenada_nombres.ver()
lista_no_ordenada_numeros.ver()

## eliminar

lista_nombre = "color"
for i in range(2):
    try:
        elemento = input(f"Ingrese el {lista_nombre} a eliminar: ").capitalize()
        lista_no_ordenada_colores.remover(elemento); continue
    except: print("ERROR: ???")

lista_nombre = "nombre"
for i in range(2):
    try:
        elemento = input(f"Ingrese el {lista_nombre} a eliminar: ").capitalize()
        lista_no_ordenada_nombres.remover(elemento); continue
    except: print("ERROR: ???")


lista_nombre = "numero"
for i in range(2):
    try:
        elemento = int(input(f"Ingrese el {lista_nombre} a eliminar: "))
        lista_no_ordenada_numeros.remover(elemento); continue
    except: print("ERROR: ???")

### mostramos las listas

lista_no_ordenada_colores.ver()
lista_no_ordenada_nombres.ver()
lista_no_ordenada_numeros.ver()

elemento_color = input("ingrese un color para agregar a la lista de colores; ")

lista_no_ordenada_colores.agregar(elemento_color)

print("la lista colores ahora es; ",)
lista_no_ordenada_colores.ver()

print("el tamaño de la lista de numeros es; ",lista_no_ordenada_numeros.tamaño())