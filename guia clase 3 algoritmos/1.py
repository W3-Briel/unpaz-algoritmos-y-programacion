# alumno: Angel Gabriel Saucedo
# Algoritmos y Programacion - B1

###########################CLASE 3################################
# Dado el siguiente programa trate de resolver cualquier error que pueda 
# producirse al ejecutarlo, resuelva con excepciones.

resultado= 0 # tiene que ser mayor a "Menor"
menor = 0
while True:
    try:
        numero_1 = int(input("Escriba un número : "))
        numero_2 = int(input("Escriba otro número: ")); break
    except ValueError:
        print("SOLO NUMEROS!! - intenta denuevo."); continue

if numero_1 == numero_2:
  print("Los dos números son iguales.")
elif numero_1 < numero_2:
  print(f"El numero1 {numero_1} es menor que {numero_2}")
  menor = numero_1
else:
  print(f"El numero2 {numero_2} es menor que {numero_1}")
  menor= numero_2
  resultado = numero_2 * numero_1
  print(f"El resultado entre {numero_1} * {numero_2} = {resultado}")
  print("*"*20)

for i in range(menor,resultado+1):
   print(i)