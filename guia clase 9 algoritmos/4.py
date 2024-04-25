# alumno: Angel Gabriel Saucedo
# Algoritmos y Programacion - B1
##########################
# Escribir una función que pida un número entero entre 1 y 10 y guarde en un fichero con el 
# nombre tabla-n.txt la tabla de multiplicar de ese número. Donde n es el número introducido. 
# Guarde en el archivo tabla-n.txt la tabla resuelta de n.

TABLA = int(input("tabla resultante del numero: "))
temporal = []

for multiplo in range(1,11):
    resultado = TABLA * multiplo
    formato = f"{TABLA} X {multiplo} = {resultado}\n"
    temporal.append(formato)
    
with open(f"tabla-{TABLA}.txt", "w+", encoding="utf-8") as file:
    file.writelines(temporal)