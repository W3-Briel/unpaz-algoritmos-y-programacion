# alumno: Angel Gabriel Saucedo
# Algoritmos y Programacion - B1
def busquedaSecuencial(lista,item):
    pos = 0
    while pos < len(lista):
        if lista[pos] == item:
            return True
        else: pos += 1
    
    return False

SECUENCIA_DESORDENADA = [1,2,32,8,17,19,42,13,0]

print(busquedaSecuencial(SECUENCIA_DESORDENADA,3))
print(busquedaSecuencial(SECUENCIA_DESORDENADA,13))

# es un algoritmo O(n)


##### siempre es mejor ordenar los elementos, antes de realizar una busqueda secuencial

def busquedaSecuencialDos(lista,item):
    pos = 0
    while pos < len(lista):
        if lista[pos] == item:
            return True
        elif lista[pos] > item: return False
        else: pos += 1
    
    return False

SECUENCIA_ORDENADA = [0,1,2,8,13,17,19,32,42]

print(busquedaSecuencialDos(SECUENCIA_ORDENADA,3))
print(busquedaSecuencialDos(SECUENCIA_ORDENADA,13))

#### y el algoritmo mas eficiente para buscar seria

def busquedaBinaria(lista,item):
    primero = 0 
    ultimo = len(lista)-1

    while primero <= ultimo:
        punto_medio = (primero + ultimo)//2
        if lista[punto_medio] == item:
            return True
        else:
            if item <lista[punto_medio]:
                ultimo = punto_medio-1
            else:
                primero = punto_medio+1
        return False

print(busquedaBinaria(SECUENCIA_ORDENADA,3))
print(busquedaBinaria(SECUENCIA_ORDENADA,13))

##### algoritmo de busqueda binaria, RECURSIVA
# tiene la ventaja de que no usa bucle, pero como es recursiva
# ocupa mucha memoria

def busqueda_binaria_recursiva(unaLista, item):
    if len(unaLista) == 0:
        return False
    else:
        punto_medio = len(unaLista)//2
        if unaLista[punto_medio]==item:
            return True
        else:
            if item<unaLista[punto_medio]: return busqueda_binaria_recursiva(unaLista[:punto_medio],item)
            else: return busqueda_binaria_recursiva(unaLista[punto_medio+1:],item)
