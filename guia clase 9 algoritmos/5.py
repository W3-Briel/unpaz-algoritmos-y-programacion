# alumno: Angel Gabriel Saucedo
# Algoritmos y Programacion - B1
##########################
# Escribir una función que pida un número entero entre 1 y 10, lea el fichero tabla-n.txt con la 
# tabla de multiplicar de ese número, donde n es el número introducido, y la muestre por pantalla. 
# Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello.

from module import io_get
from module import _functions

def mostrarOcrearTabla():
    tablaElegida = _functions.entre1Y10("un número entero entre 1 y 10: ")
    try:
        with open(f"tabla-{tablaElegida}.txt","r") as tabla:
            print(f"el fichero de 'tabla del {tablaElegida}' ya se encontraba creada.\n")
            print(tabla.read())
    except:
        with open(f"tabla-{tablaElegida}.txt","w+") as tabla:
            io_get.tablaN(tablaElegida)
            tabla.seek(0)
            print(f"el fichero de 'tabla del {tablaElegida}' no se encontraba creada.\n")
            print(tabla.read())

mostrarOcrearTabla()