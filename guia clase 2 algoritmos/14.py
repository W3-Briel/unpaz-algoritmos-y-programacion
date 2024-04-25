# alumno: Angel Gabriel Saucedo
# Algoritmos y Programacion - B1

######################## FUNCIONES RECURSIVAS #########################

## Dada una secuencia de caracteres, obtener dicha secuencia invertida.

string = "hola"
print(string[-1]+string[:-1])

def invertir_string(string):
    if len(string) == 0:
        return string
    else:
        string_invertido = string[-1] + invertir_string(string[:-1])
        return string_invertido

print(invertir_string(input("ingrese una cadena de texto a invertir: ")))