# alumno: Angel Gabriel Saucedo
# Algoritmos y Programacion - B1

import array as arr
############################## ARRAYS #############################
# Escriba un programa que cargue un vector desde el número 100 al 200, debe utilizar 2 métodos 
# de carga, usando range y otro utilizando while, luego muestre los valores uno al lado del otro.


#inicializamos y cargamos el vector
vector = arr.array("i",[])

# metodo 1

for numero in range(100,150):
    vector.append(numero)

# metodo 2
numero_while = 150
while len(vector) < 100:
    vector.append(numero_while)
    numero_while += 1

#output
print(*vector) # los dos metodos en total, cargan los 100 numeros al vector.