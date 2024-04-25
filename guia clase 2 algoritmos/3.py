# alumno: Angel Gabriel Saucedo
# Algoritmos y Programacion - B1

import array as arr
############################## ARRAYS ##############################
# Escriba un programa que permita cargar por teclado un vector de 10 posiciones, con números 
# enteros, luego debe mostrar los números pero si el número termina en 3 8 4 9 debe agregar 
# un * antes de mostrar el número (investigue cómo obtener un ultimo digito de un número).

# control
NUMEROS_CENSURADOS = (3,4,8,9)

# inicializamos y cargamos vector. trabajando excepciones.
vector = arr.array("i", [])

def cargando_datos():
    for indice in range(10):
        try:
            numero = int(input(f"Posicion Nª{indice+1}, que numero deseas agregar: "))
            vector.append(numero)
        except ValueError:
            print("REINICIANDO LA CARGA DE DATOS!!, solo numeros.")
            cargando_datos()

cargando_datos()

# output
for valor in vector:
    ultimo_digito = valor % 10
    if ultimo_digito in (NUMEROS_CENSURADOS):
        print("***",valor)
    else:
        print(valor)