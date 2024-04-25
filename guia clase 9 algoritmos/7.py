# alumno: Angel Gabriel Saucedo
# Algoritmos y Programacion - B1
##########################
# Título: Búsqueda textual
# Dado el archivo de texto cancion.txt, brindado por el profesor,
# realice la descarga y guárdelo en el mismo path donde creará su programa.
# ● Muestre todo el texto en pantalla
# ● Solicite al usuario un texto a buscar.
# ● Analice el archivo, busque y encuentre dentro del archivo el texto buscado
# imprima por pantalla todas las líneas completas donde aparezca el texto.
# ● Atención, el texto buscado no debe ser sensible a mayúsculas o minúsculas.
# ● Devuelva cuantas veces se encontró el texto introducido en el total del archivo
# ● Si no hubiera coincidencia deberá avisar.
# Atención cuando abra el archivo utilice la codificación utf8
# with open(nombre_archivo,'r',encoding='utf8') as xxxx :

ARCHIVO = "cancion.txt"

def mostrarTexto(archivo):
    with open(archivo,"r",encoding="utf-8") as file: print(file.read())
    del file

def busquedaTextual(archivo,palabra):
    with open(archivo,"r",encoding="utf-8") as file:
        array_lineas = file.readlines()
        coincidencias = []
        for numeroDeLinea,contenidoDeLinea in enumerate(array_lineas):
            if str(palabra).lower() in contenidoDeLinea.lower():
                coincidencias.append((numeroDeLinea,contenidoDeLinea[:-1]))
        if len(coincidencias) == 0: return print("no se encontraron coincidencias")
        
        print(f"se encontraron {len(coincidencias)} coincidencia:")
        for linea in coincidencias:
            print(f"en la linea {linea[0]+1}:\ncontenido: {linea[1]}")
    del file

try:
    mostrarTexto(ARCHIVO)
    busquedaTextual(ARCHIVO,input("que texto deseas buscar?: "))
except: print(" wtf")