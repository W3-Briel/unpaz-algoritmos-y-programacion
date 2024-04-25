# Ejercicio 2:

# Ver el nuevo TDA para el parcial: ListaORDENADA_parcial.py
# Combinados = ['CUATRO', 2, 3, 'CINCO', 'SEIS', 4, 'NUEVE', 'DOS', 'CERO', 'TRES', 6, 'SIETE', 9, 5, 'UNO', 'OCHO', 1, 7, 8]
 
# A. Agregue a una lista ordenada(PDA), la lista de datos propuesta llamada Combinados. Muestre la lista creada.
# B. Que procedimiento debería incorporar para que la lista Combinados pueda ser ordenada por ListaORDENADA_parcial

#      Explique porque se ordenaron los elementos que son palabras, de esa forma.

# C. Explique qué función cumple el método: metodo_nuevo
# D. Realice una operación donde se ponga en práctica el método metodo_nuevo
# E. Cree un método para limpiar(eliminar) la lista creada. Muestre la lista eliminada.
from ListaORDENADA_parcial import  *

Combinados = ['CUATRO', 2, 3, 'CINCO', 'SEIS', 4, 'NUEVE', 'DOS', 'CERO', 'TRES', 6, 'SIETE', 9, 5, 'UNO', 'OCHO', 1, 7, 8]

mi_lista_ordenada = ListaOrdenada()

## carga de datos
for dato in Combinados:
    mi_lista_ordenada.agregar(str(dato))
## los elementos "Combinados" se ordenan de manera alfabetica.
print(mi_lista_ordenada.ver())

print("\nUtilizando el metodo nuevo!!")

for indice in range(mi_lista_ordenada.tamano()):
    print(f"el elemento '{mi_lista_ordenada.metodo_nuevo(indice)}', esta en el indice {indice}")

print("El 'metodo nuevo' es una especie de buscador por indice, de nuestra lista ordenada.\n")

print(f"la lista a borrar es,\n")
mi_lista_ordenada.ver()
print(mi_lista_ordenada.borrar_lista())
print(f"la lista ahora es,\n")
mi_lista_ordenada.ver()