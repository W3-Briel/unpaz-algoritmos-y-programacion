# alumno: Angel Gabriel Saucedo
# Algoritmos y Programacion - B1

############ ESTRUCTURAS DE DECISION ANIDADAS IF ELIF ELSE ############

##14 Escribir un programa que permita realizar 3 cálculos aritméticos, suma, resta y multiplicación. 
## Las opciones deben presentarse a modo de menú de opciones , el usuario elegirá la operación 
## deseada, el programa deberá verificar si el valor ingresado esta entre las opciones del menú 
## , si la opción ingresada no es correcta debe mostrar un mensaje que diga opción incorrecta y 
## salir del programa pero si la opción es correcta seguirá con el programa y se le pedirá al 
## usuario el ingreso de dos números enteros para ejecutar la operación seleccionada, luego debe 
## mostrar la operación seleccionada, el desarrollo y el resultado. ejemplo : 
## Menú: 
## Suma (1) Resta (2) Multiplicación (3) 
## opción: 1 
## dato : 1 
## dato : 2 
## El resultado de la suma 1 + 2 = 3.

menu_texto = int(input("Menu\n Suma (1) Resta (2) Multiplicación (3): "))
print("opcion:", menu_texto)
if menu_texto in (1,2,3):
    dato_1,dato_2 = int(input("nro 1: ")),int(input("nro 2: "))
    match menu_texto:
        case 1:
            print(f"{dato_1}+{dato_2}={dato_1+dato_2}")
        case 2:
            print(f"{dato_1}-{dato_2}={dato_1-dato_2}")
        case 3:
            print(f"{dato_1}*{dato_2}={dato_1*dato_2}")
else:
    print("opcion incorrecta!!")