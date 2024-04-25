# alumno: Angel Gabriel Saucedo
# Algoritmos y Programacion - B1
####################################
# Cree un programa que lee datos desde un archivo, los procesa y luego escribe el resultado
# en otro archivo. Suponga que tiene un archivo llamado "entrada.txt" con números enteros
# separados por comas, y desea calcular la suma de estos números y escribir el resultado en
# un archivo llamado "salida.txt". 

with open("entrada.txt","r", encoding="utf-8") as entrada:
    numeros = entrada.read()
    sumaTotal = 0
    for numero in numeros.split(","):
        try:
            sumaTotal+= int(numero)
        except ValueError: 
            print("OCURRIO UN ERROR, revisar el contenido de entrada", ValueError)
            sumaTotal = "NaN/ERROR"

del entrada

with open("salida.txt","w", encoding="utf-8") as salida:
    salida.write(f"la suma de los numeros es {sumaTotal}")