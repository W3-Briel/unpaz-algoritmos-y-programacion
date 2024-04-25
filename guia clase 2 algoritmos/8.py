# alumno: Angel Gabriel Saucedo
# Algoritmos y Programacion - B1

############################ FUNCIONES ############################
# Confeccionar una función que reciba tres enteros y los muestre ordenados de menor a
# mayor. En otra función solicitar la carga de 3 enteros por teclado y proceder a llamar a la
# primera función definida.

def tres_enteros_menor_a_mayor(int1,int2,int3):
    sin_ordenar = [int1,int2,int3]
    ordenados = [None,None,None]
    # process
    for numero in sin_ordenar:
        if numero is min(sin_ordenar): ordenados[0] = min(sin_ordenar)
        elif numero is max(sin_ordenar): ordenados[2] = max(sin_ordenar)
        else: ordenados[1] = numero
    #output
    return print("los numeros ordenados de menor a mayor son; ",*ordenados)

# inputs
def ingresar_tres_numeros():
    lista_de_numeros = []
    for i in range(3):
        try:
            numero = int(input(f"Ingrese el valor Nª{i+1}: "))
            lista_de_numeros.append(numero)
        except ValueError:
            print("SOLO INGRESE NUMEROS, intentemos denuevo.")
            ingresar_tres_numeros()
    # output
    print("los numeros ingresados son: ",*lista_de_numeros)
    return tres_enteros_menor_a_mayor(lista_de_numeros[0],lista_de_numeros[1],lista_de_numeros[2])

# funcion main
ingresar_tres_numeros()