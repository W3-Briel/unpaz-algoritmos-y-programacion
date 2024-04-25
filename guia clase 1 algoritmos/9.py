# alumno: Angel Gabriel Saucedo
# Algoritmos y Programacion - B1

############ CADENAS ############

##9 Escribir un programa que muestre cuántos caracteres tiene su nombre completo

nombre_completo = input("cual es tu nombre completo?")
contador_de_caracteres = 0

for caracter in nombre_completo:
    if caracter != " ":
        contador_de_caracteres += 1

print("los caracteres de tu nombre completo son ",contador_de_caracteres) # salida compuesta