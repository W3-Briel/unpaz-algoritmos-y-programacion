# alumno: Angel Gabriel Saucedo
# Algoritmos y Programacion - B1

############################ FUNCIONES ############################
# Confeccionar una función que reciba tres enteros y nos muestre el mayor de ellos. La carga 
# de los valores se hace por teclado.

# inicializamos
lista_de_numeros = []

# trabajamos excepciones
def cargando_datos():
    for i in range(3):
        try:
            numero = int(input(f"Ingrese el valor Nª{i+1}: "))
            lista_de_numeros.append(numero)
        except ValueError:
            print("SOLO INGRESE NUMEROS, intentemos denuevo.")
            cargando_datos()

def maximo_list(lista):
    return print("el maximo es: ",max(lista))

#output - llamada a las funciones

cargando_datos()
maximo_list(lista_de_numeros)