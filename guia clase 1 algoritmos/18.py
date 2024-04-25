# alumno: Angel Gabriel Saucedo
# Algoritmos y Programacion - B1

############ ESTRUCTURAS ITERATIVAS FOR ############

##18 Escribir un programa que solicite una palabra y la muestre letra por letra separada por un 
## guión, en una misma línea de texto ( renglón) , use “end”. 
## por ejemplo: 
## azul 
## a-z-u-l-

palabra = input("ingrese una palabra: ")
for letra in palabra: print(letra, end="-")