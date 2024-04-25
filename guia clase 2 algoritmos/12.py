# alumno: Angel Gabriel Saucedo
# Algoritmos y Programacion - B1

######################## FUNCIONES RECURSIVAS #########################
# implementar una función para calcular el producto de dos números enteros dados.

# recursividad
def producto_recursivo(numero_a,numero_b):
    if numero_b == 0:
        return 0
    return numero_a + producto_recursivo(numero_a,numero_b-1)

#input - excepciones

while True:
    try:
        numero_a = int(input("ingresa un factor: "))
        while True:
            try:
                numero_b = int(input("ingresa otro factor: "))
                if numero_b < 0: print("uno positivo por favor...");continue
                else: break
            except ValueError:
                print("solo numeros!!, intenta denuevo")
        break
    except ValueError:
        print("solo numeros!!, intenta denuevo"); continue

print(producto_recursivo(numero_a,numero_b)," es la multiplicacion de ambos factores.")