# alumno: Angel Gabriel Saucedo
# Algoritmos y Programacion - B1

############ ESTRUCTURAS DE DECISION DOBLE IF ELSE ############

##13 Escribir un programa que permita calcular la suma de tres números enteros ingresados por 
## teclado. Si el resultado es mayor a 50 dividir por 2 ,En caso contrario elevar el resultado al 
## cubo, si al calcular el cubo el resultado es superior a 5000 deberá mostrar por pantalla “Este 
## es un gran número”

numero1,numero2,numero3 = int(input("Ingrese, tres numeros a sumar;\n\tnro1; ")),int(input("\tnro2; ")),int(input("\tnro3; "))
suma_total_3_numeros = numero1 + numero2 + numero3

if suma_total_3_numeros > 5000:
    print("Este es un gran numero")
elif suma_total_3_numeros < 50:
    print(f"El resultado es {suma_total_3_numeros}, y como es mayor a 50, lo dividermos en 2: nos queda '{suma_total_3_numeros/2}'.")
else:
    print(f"el resultado es {suma_total_3_numeros}, y como es menor a 50, lo elevamos al cuadrado: nos queda '{suma_total_3_numeros**2}'.")