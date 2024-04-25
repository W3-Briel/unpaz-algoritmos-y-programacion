#imprimir de un numero dado, todos los numeros enteros hasta el cero.

## CASO BASE: El caso mas simple o el ultimo caso. en este ejemplo es imprimir el 0.

## CASO RECURSIVO: la funcion se llama asi misma, pero resolviendo un problema.


numero = 10

def todos_los_numeros_al_cero(nuemero_inicial):
    if nuemero_inicial == 0: # caso base
        print(nuemero_inicial)
    else: #caso recursivo
        print(nuemero_inicial)
        todos_los_numeros_al_cero(nuemero_inicial-1)

todos_los_numeros_al_cero(numero)