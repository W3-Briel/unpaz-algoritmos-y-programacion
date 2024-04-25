# alumno: Angel Gabriel Saucedo
# Algoritmos y Programacion - B1
##########################
# Realizar un programa que realice los ejercicios 1 y 2 utilizando la estructura with.
from module import io_get

FRASE = "Este es el ejercicio 3"

with open("archivo.txt","w+",encoding="utf-8") as file:
    file.write(FRASE)
    print(io_get.parseInfo(file))