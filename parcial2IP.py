# import random as r

# 1. Un año bisiesto es aquel divisible por 4, excepto aquellos divisibles por 100 pero
# no por 400. Escribe un programa que solicite al usuario un año y determine si es
# bisiesto o no, y que finalice el programa hasta que el usuarix coloque “Salir” o el
# número 0.

# not (a % 4) and (a % 100 or not a % 400) -> año bisiesto(lo saque de google)!!

## (año % 100) == 0 AND (año % 400) != 0 -> año no bisiesto??
## (año % 4) == 0 -> bisiesto

# def bisiesto(año):
#     if ((año % 100) == 0) & ((año % 400) != 0):
#         return f"no es bisiesto el año {año}"
#     elif ((año % 4) == 0):
#         return f"es bisiesto el año {año}"

# while True:
#     print(bisiesto(int(input("ingresa el año!: "))))
#     if input("ingresa 'salir' o '0' para salir del programa: ") in ("salir","0"): break

# 2. En una tienda, hay descuentos en función del total de compra. Escribe un
# programa que solicite al usuario el total de la compra y aplique automáticamente
# el descuento correspondiente según la siguiente tabla: 10% de descuento para
# compras mayores o iguales a $100, 20% para compras mayores o iguales a $200,
# y 30% para compras mayores o iguales a $300. Que finalice el programa hasta
# que el usuarix coloque “Salir” o el número 0.

# total de la compra

# descuentos: tota >= 100 (10%), total>= 200 (20%), total >= 300 (30%)

# total de compra - descuento.

# salir?

# def con_descuento(total):
    
#     if total >= 300:
#         return total * 0.70
#     elif total >= 200:
#         return total * 0.80
#     elif total >= 100:
#         return total * 0.90
#     else:
#         return f" {total}, no hay descuento!"

# while True:
#     total = int(input("ingresa el total gastado: "))

#     print("tienes que pagar: ",con_descuento(total))
#     if input("ingresa 'salir' o '0' para salir del programa: ") in ("salir","0"): break

# 3. Considere que necesitamos un programa que realice conversiones entre diferentes
# unidades de medida. El programa debe solicitar al usuario una cantidad y una
# unidad de medida (metros, centímetros o pulgadas), y luego realizar la conversión
# a las otras dos unidades de medida.
# El programa debe ejecutarse en un bucle continuo hasta que el usuario ingrese el
# valor 0 como cantidad. Cada vez que se solicite una cantidad y una unidad de
# medida, el programa debe mostrar los resultados de las conversiones a metros,
# centímetros y pulgadas. A continuación, se muestra un ejemplo de la interacción
# esperada:
######### (aca hay una foto en el pdf)
# El programa debe realizar las conversiones según las siguientes relaciones:
#  1 metro equivale a 100 centímetros y a aproximadamente 39.37 pulgadas.
#  1 centímetro equivale a 0.01 metros y a aproximadamente 0.3937 pulgadas.
#  1 pulgada equivale a aproximadamente 0.0254 metros y a 2.54. centímetros.

# unidad de medida (metros, centímetros o pulgadas)

# def convertir(valor, unidad):
#     metro_cm = 100
#     metro_pg = 39.37

#     centimetro_met = 0.01
#     centimetro_pg = 0.3937

#     pulgada_met = 0.0254
#     pulgada_cm = 2.54

#     if unidad == "centimetro":
#         print(f" {valor} {unidad} e quivale a {valor*centimetro_met} metro")
#         print(f" {valor} {unidad} e quivale a {valor*centimetro_pg} pulgada")
    
#     if unidad == "metro":
#         print(f" {valor} {unidad} e quivale a {valor*metro_cm} centimetro")
#         print(f" {valor} {unidad} e quivale a {valor*metro_pg} pulgada")

#     if unidad == "pulgada":
#         print(f" {valor} {unidad} e quivale a {valor*pulgada_cm} centimetro")
#         print(f" {valor} {unidad} e quivale a {valor*pulgada_met} metro")

# while True:
#     valor = input("ingrese el valor o '0' para salir: ")
#     if valor == "0": print("chau"); break
#     convertir(int(valor),input("unidad de medida (metro, centrimetro, pulgada): ")) ## se pueden trabajar try except


# 4. Conversor de sistema decimal a binario: Introducción: Escribe un programa que
# solicite al usuario un número en sistema decimal y lo convierta a su representación
# en sistema binario.

# def deabi(numero):
#     restos=[]
#     while numero != 0:
#         modulo= numero % 2 
#         cociente= numero//2
#         restos.append(modulo)
#         numero= cociente
#     return restos[::-1]

# numero=int(input('Ingrese un número: '))

# print(*deabi(numero)) ## metodo uno con funcion

# print(f"{str(bin(numero))[2::]}") ## metodo con funcion integrada de python

# 5. Escribe un programa que elija aleatoriamente una palabra de una lista de palabras
# predefinidas. Luego, permite al usuario adivinar las letras de la palabra en un
# juego de ahorcado. El programa debe mostrar en pantalla el estado actual del juego
# (letras adivinadas y letras por adivinar) y permitir al usuario ingresar una letra en
# cada intento.

# def letras_diferentes(palabra):
#     l_diferentes = ""
#     for letra in palabra:
#         if letra not in l_diferentes: l_diferentes+=letra

#     return (len(l_diferentes),l_diferentes)

# PALABRAS = ["Angel","Denise","AUTO","moto","cancha",'Escribe', 'programa',"pelota","messi","maradona",
#             'elija', 'aleatoriamente', 'palabra,', 'lista', 'palabras', 'predefinidas'] # -> las letras de las palabras deberian estar en minusculas
# MAX_ERRORES = 3


# palabra_elegida = r.choice(PALABRAS).lower()
# palabra_info = letras_diferentes(palabra_elegida)

# letras_cantadas = []

# for i in palabra_elegida: print("_", end=" ")

# fallas = MAX_ERRORES
# while fallas > 0:

#     if set(letras_cantadas).issuperset(palabra_info[1]):
#         print()
#         print("*"*10,f"\neu ganaste\npalabra: {palabra_elegida}\n","*"*10); break

#     letra = input(f"vidas: {fallas}| ingresar una letra: ").lower()
    
#     if letra in letras_cantadas: print("ya la dijiste capo.\n"); continue ## si la letra ya esta cantada, solo continua
    
#     cantar_letra = letras_cantadas.append(letra[0])
#     for i in palabra_elegida:
#         if i in letras_cantadas: print(i, end=" ")
#         else: print("_", end=" ")

#     if letra in palabra_info[1]: continue

#     fallas-=1

# if fallas == 0: print("\nPERDEDOR ERA OBVIO!: ",palabra_elegida)

# 6. Mencione las diferencias entre if, elif, else, while, y for.

#if -> estructura condicional que solo entra al scope si se cumple la condicional(?)
#elif -> es parte de la estructura condicional del if, no se puede poner en el medio nada(osea va el if antes)
# y tambien ejecuta lo de su scope, solo si se cumple su condicional (igual al if)
## el detalle es que no se llega al elif, sin pasar por el if. si la condicion if se cumple, no evaluaria en el elif(algo asi)

# while -> bucle indefinido. inicialmente no sabemos cuantas veces se podria llegar a iterar. podemos utilizar palabras como break y continue
# puede llevar una condicional en su estructura

# for -> bucle exacto o definido??. sabemos cuantas veces llega a iterar y tambien podemos utilizar break y continue.
# una variable iterativa que es recorrida por cada valor.

## detalle. se podria utilizar un while como un for. pero no se puede utilizar un for como un while.