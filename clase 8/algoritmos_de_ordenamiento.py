# alumno: Angel Gabriel Saucedo
# Algoritmos y Programacion - B1
secuencia_desordenada = [1,2,32,8,17,19,42,13,0]

##### O(n^2)

def ordenamiento_burbuja(una_lista):
    for num_pasada in range(len(una_lista)-1,0,-1):
        for i in range(num_pasada):
            if una_lista[i]>una_lista[i+1]:
                una_lista[i], una_lista[i+1] = una_lista[i+1], una_lista[i]

# print(secuencia_desordenada)
# ordenamiento_burbuja(secuencia_desordenada)
# print(secuencia_desordenada)

#########

def ordenamiento_por_seleccion(una_lista):
    for llenar_ranura in range(len(una_lista)-1,0,-1):
        posicion_del_mayor = 0
        for ubicacion in range(1,llenar_ranura+1):
            if una_lista[ubicacion] > una_lista[posicion_del_mayor]:
                posicion_del_mayor = ubicacion
        una_lista[llenar_ranura], una_lista[posicion_del_mayor] = una_lista[posicion_del_mayor], una_lista[llenar_ranura]

print(secuencia_desordenada)
ordenamiento_burbuja(secuencia_desordenada)
print(secuencia_desordenada)