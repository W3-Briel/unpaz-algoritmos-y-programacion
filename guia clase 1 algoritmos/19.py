# alumno: Angel Gabriel Saucedo
# Algoritmos y Programacion - B1

############ ESTRUCTURAS ITERATIVAS FOR ############

##19 Escribir un programa que solicite un número entero positivo, que muestre los múltiplos de 5
## que existen entre el número ingresado y su multiplicación por 30. por ejemplo: entre 3 y (3*30)

input_numero = int(input("ingrese un numero entero positivo; "))
if input_numero >= 0: numero = input_numero

numero_multiplos = []
numero_maximo = numero*30

for multiplo in range(1, numero_maximo+1):
    tabla = numero * multiplo
    if tabla <= numero_maximo: numero_multiplos.append(tabla)

print("la lista de numeros multiplos de {} hasta {} son los siguientes; ".format(numero,numero_maximo))
print(*numero_multiplos)