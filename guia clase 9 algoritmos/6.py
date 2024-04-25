# alumno: Angel Gabriel Saucedo
# Algoritmos y Programacion - B1
##########################
# Escribir una función que pida dos números n y m entre 1 y 10, lea el fichero tabla-n.txt con la
# tabla de multiplicar de ese número, y muestre por pantalla la línea m del fichero. Si el fichero
# no existe debe mostrar un mensaje por pantalla informando de ello.

from module import _functions
from module import io_get

def encontrarEnTabla(tabla,multiplo):
    with open(f"tabla-{tabla}.txt","r") as tablaArchivo:
            ubicacion = tablaArchivo.readlines()[int(multiplo)-1]
            print("el resultado encontrado en esa ubicacion es:")
            print(ubicacion)
    del tablaArchivo

def buscarEnTabla():
    TABLA = _functions.entre1Y10("elige una tabla entre el 1 y 10: ")
    multiplo = _functions.entre1Y10("elige un multiplo el 1 y 10: ")
    try:
        encontrarEnTabla(TABLA,multiplo)
    except:
        print("ERROR - no se encuentra esa tabla creada.")
        confirmar = _functions.confirmar("deseas crear una tabla y mostrar esa ubicacion?: (SI) o (NO)")
        if confirmar:
            io_get.tablaN(TABLA)
            return encontrarEnTabla(TABLA,multiplo)
        print("ok, cancelamos la creacion...")

buscarEnTabla()