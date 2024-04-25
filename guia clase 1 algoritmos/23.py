# alumno: Angel Gabriel Saucedo
# Algoritmos y Programacion - B1

############ ESTRUCTURAS ITERATIVAS FOR ANIDADAS ############

##23 Escribir un programa muestre las tablas del 1 al 10 en formato pitagórico 
## 1 2 3 4 5 6 7 8 9 10 
## 2 4 6 8 10 12 14 16 18 20 
## 3 6 9 12 15 18 21 24 27 30

for tabla in range(1,11):
    for multiplo in range(1,11):
        if multiplo == 10:
            print(tabla*multiplo)
        else:
            resutado = str(tabla*multiplo).zfill(2)
            print(resutado, end=" ")