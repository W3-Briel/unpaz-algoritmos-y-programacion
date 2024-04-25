# alumno: Angel Gabriel Saucedo
# Algoritmos y Programacion - B1

############ ESTRUCTURAS ITERATIVAS FOR ANIDADAS ############

##22 Escribir un programa que solicite muestre las tablas del 1 al 9 utilice for anidados.

for tabla in range(1,10):
    print("tabla del ",tabla)
    for multiplo in range(1,11):
        print(f"{tabla} * {multiplo} = {tabla*multiplo}")