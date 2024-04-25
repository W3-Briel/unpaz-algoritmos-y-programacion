# alumno: Angel Gabriel Saucedo
# Algoritmos y Programacion - B1
##########################
# Crear un programa que abra el fichero editado anteriormente y muestre el estado del fichero,
# el modo en el que fue abierto, el nombre y la codificación de caracteres del mismo.

from module import io_get

archivo = open("archivo.txt","r")
print(io_get.parseInfo(archivo))