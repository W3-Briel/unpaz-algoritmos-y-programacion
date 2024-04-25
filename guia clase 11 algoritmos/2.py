# alumno: Angel Gabriel Saucedo
# Algoritmos y Programacion - B1
####################################
# Cree un programa que lea un archivo de texto, cuente la cantidad de palabras en el archivo
# y luego escriba el resultado en otro archivo. Suponga que tiene un archivo de texto llamado
# "entrada2.txt" con el siguiente contenido:

# Python es un lenguaje de programación muy poderoso y versátil.
# Es ampliamente utilizado en diversas aplicaciones, incluyendo desarrollo web, análisis de
# datos y aprendizaje automático.
# A continuación, cree un programa para contar las palabras en este archivo y escribir el
# resultado en un nuevo archivo llamado "resultado2.txt":

with open("entrada2.txt","r") as entrada:
    largo = len(entrada.read().split(" "))
    with open("resultado2.txt","w",encoding="utf-8") as resultado:
        resultado.write(str(largo))