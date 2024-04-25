# alumno: Angel Gabriel Saucedo
# Algoritmos y Programacion - B1
##########################

def entre1Y10(inputText):
    while True:
        tablaDel = int(input(inputText))
        if tablaDel <= 10 and tablaDel >= 1:
            return tablaDel
        print("debe ser un numero entre 1 y 10... QUE SEA ENTERO!")

def numeroIterable(inputText):
    while True:
            try:
                cantidad = int(input(inputText))
                if cantidad > 0: return cantidad
                print("no puedes ingresar esa cantidad!")
            except ValueError: print("ERROR, INGRESA SOLO LA CANTIDAD", ValueError)

def confirmar(inputText):
    confirmar = input(inputText).upper()
    match confirmar:
        case "SI":
            return True
        case _:
            return False