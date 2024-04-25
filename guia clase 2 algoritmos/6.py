# alumno: Angel Gabriel Saucedo
# Algoritmos y Programacion - B1

############################ FUNCIONES ############################
# Desarrollar un programa que permita ingresar el lado de un cuadrado. Luego preguntar si
# quiere calcular y mostrar su perímetro o su superficie. 

# trabajando excepciones, primer input.
while True:
    try:
        lado_del_cuadrado = int(input("ingresa un lado del cuadrado: ")); break
    except ValueError:
        print("SOLO INGRESA NUMEROS!!, intenta denuevo."); continue

# trabajando operaciones.
while True:
    operaciones = input("quiere calcular (P)arametro o (S)uperficie: ").upper()
    match operaciones:
        case "P":
            print(lado_del_cuadrado*4, " es el largo del cuadrado"); break
        case "S":
            print(lado_del_cuadrado**2, " es la superficie en mt2"); break
        case _:
            print("caso por defecto, no es P ni S"); continue