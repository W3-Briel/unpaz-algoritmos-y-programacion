# alumno: Angel Gabriel Saucedo
# Algoritmos y Programacion - B1
##########################
# Crear un programa que abra un fichero en modo lectura y escritura, si no existe lo creará, y
# añadir la frase ‘Este es el ejercicio 1’.

FRASE = "Este es el ejercicio 1"
archivo = open("archivo.txt", "w+",encoding="utf-8") # tenemos que utilizar primero el de escribir, ya que de lo contrario intentaria leer un archivo que no existe
archivo.write(FRASE)

archivo.close()