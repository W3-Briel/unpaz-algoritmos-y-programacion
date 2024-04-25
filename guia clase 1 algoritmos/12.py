# alumno: Angel Gabriel Saucedo
# Algoritmos y Programacion - B1

############ ESTRUCTURAS DE DECISION DOBLE IF ELSE ############

##12 Escribir un programa que permita el ingreso de 2 dígitos, si es menor a 50 debe mostrar la 
## mitad de ese número.
NUMERO = int(input("ingresa un numero de dos digitos; "))

if NUMERO < 50:
    print(f"el numero es {NUMERO} y su mitad; {NUMERO/2}")
elif (NUMERO > 99) | (NUMERO < -99):
    print("solo dos digitos")