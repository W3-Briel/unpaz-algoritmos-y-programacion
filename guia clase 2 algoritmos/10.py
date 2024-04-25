# alumno: Angel Gabriel Saucedo
# Algoritmos y Programacion - B1

import array as arr
############################ FUNCIONES ############################
# Escriba una función para cargar un vector con n cantidad de elementos con valores 0 y 1
# correlativamente , luego debe retornar el vector.
# Para probar la función escriba un programa que solicite al usuario la cantidad de elementos
# para el vector este número debe ser entero positivo, Utilice la función integrada de python
# .isnumeric() para verificar, ejemplo: mi_numero.isnumeric() devuelve True o False, si es
# correcto debe llamar a la función y devolver el vector con los elementos pedidos y luego
# debe mostrar los elementos del vector uno debajo del otro por pantalla pero si es incorrecto
# debe volver a solicitar un nuevo número, antes controle y avise que hubo un error.

while True:
    cantidad_de_elementos = input("cantidad de elementos del vector?: ")
    iterable = cantidad_de_elementos.isnumeric()
    if iterable: break
    else: print("tiene que ser un numero entero positivo; "); continue

def ceros_y_unos(largo):
    vector = arr.array("i",[])
    ultimo_agregado = 1

    for i in range(int(largo)):
        if ultimo_agregado == 1: ultimo_agregado = 0; vector.append(0)
        else: ultimo_agregado = 1; vector.append(1)
    
    for numero in vector:
        print(numero)

ceros_y_unos(cantidad_de_elementos)