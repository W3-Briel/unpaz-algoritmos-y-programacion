# alumno: Angel Gabriel Saucedo
# Algoritmos y Programacion - B1
from time import time
############## suma con iteraciones
# def sumaDeN2(n):
#     inicio = time()

#     laSuma = 0
#     for i in range(1,n+1):
#         laSuma = laSuma +i
    
#     final = time()
#     return laSuma,final-inicio

# resultado = sumaDeN2(100000)
# print(f"{resultado[0]:15d} y requirio {resultado[1]:.10f} segundos")

############# suma directa sin iteraciones - MUCHO MAS RAPIDO
# def sumaDeN3(n):
#     return (n*(n+1))//2

# inicio = time()

# resultado = sumaDeN3(10000000000000000000000000000)

# fin = time()

# tiempo = fin - inicio
# print(inicio,fin)
# print(f"La suma es {resultado:15d} y requirio {tiempo:.10f} segundos")