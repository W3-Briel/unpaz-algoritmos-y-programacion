# alumno: Angel Gabriel Saucedo
# Algoritmos y Programacion - B1

############ ESTRUCTURAS ITERATIVAS WHILE ############

##16 Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la 
## cuenta atrás desde ese número hasta cero separados por comas. (Investigue cómo mostrar 
## datos con print en la misma línea de texto), Si se anima trate de no imprimir la última coma 
## después del 0. 
## Ejemplo: 5 
## 5,4,3,2,1,0, 
## 5,4,3,2,1,0

numero = int(input("ingrese un numero positivo: "))

while numero >= 0:
    diferente_a_cero = numero != 0
    if diferente_a_cero:
        print(numero, end=", ")
    else:
        print(numero)
    numero -=1