# alumno: Angel Gabriel Saucedo
# Algoritmos y Programacion - B1

###########################CLASE 3################################
# Dado el siguiente código verificar si está bien escrito resuelva todo lo que se 
# pueda manualmente y agregue las excepciones necesarias.

divisor = 1 
acumulador = 0 
listado_numeros=[]

while True:
    try:
        numero_input = input("Ingrese un numero para calcular y mostrar sus divisores: ")
        numero = int(numero_input)
        if int(numero_input) < 0:
            print("Debe ingresar un valor numérico entero positivo"); continue
        elif numero_input.isnumeric(): print(f"Los numeros divisores de {numero_input} son: "); break
    except ValueError: print("SOLO NUMEROS!!! intenta denuevo."); continue

while divisor <= numero:
    if numero % divisor == 0:
        acumulador += divisor
        listado_numeros.append(divisor)

    divisor +=1

for i in range(len(listado_numeros)):
    print(f"{listado_numeros[i]:^30d}")

print(f"La suma de todos los divisores es de {acumulador}")