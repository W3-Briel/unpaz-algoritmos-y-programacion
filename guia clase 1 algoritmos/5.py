# alumno: Angel Gabriel Saucedo
# Algoritmos y Programacion - B1

############ OPERADORES ARITMETICOS ############

##5 Escribir un programa que calcule el área de un triángulo, sabiendo que :
## ● La base (b) mide 20.5
## ● La altura (h) es igual a la base al cuadrado
## Investigue cual es la fórmula para calcular el área de un triángulo y utilicela en el programa
## luego muestre por pantalla el resultado.

# definimos nuestro triangulo
base_del_triangulo = 20.5
altura_del_triangulo = base_del_triangulo ** 2
# guardamos el area en una variable
area_del_triangulo = (base_del_triangulo * altura_del_triangulo)/2
# mostramos en pantalla
print("el area del triangulo es",area_del_triangulo)