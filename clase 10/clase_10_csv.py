# alumno: Angel Gabriel Saucedo
# Algoritmos y Programacion - B1
import csv

alumnos = [
    ("Manuel", "Aprobo", 4,7),
    ("Lorena", "Desaprobo", 3,0),
    ("Javier", "Aprobado", 7,7),
    ("Marta", "Desaprobada", 4,3)
]

with open("alumnos.csv","w", newline="\n") as arch_csv:
    writer = csv.writer(arch_csv, delimiter=";")
    encabezado = ["Nombre","TP","N_P1","N_P2"]
    writer.writerow(encabezado)
    for alum in alumnos:
        writer.writerow(alum)