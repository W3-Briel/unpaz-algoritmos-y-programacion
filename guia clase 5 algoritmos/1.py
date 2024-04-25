# alumno: Angel Gabriel Saucedo
# Algoritmos y Programacion - B1
###################################################
#1. A partir del programa realizado de Pila, Realice un programa a base de menú, con las opciones
#:
    #1. Apilar nombre (ingrese nombre por teclado, la primera letra debe estar en mayúsculas), al ingresar a esta opción ingresa los nombres repetidamente, sólo dejará de ingresar
    #nombres si ingresa un nombre vacío (Enter) para volver al menú.
    #2. Desapilar nombre
    #3. Salir
#Antes de terminar debe mostrar todos los nombres de la pila en forma vertical (uno debajo de
#otro) debe crear otro método para cumplir con este enunciado. El primer nombre debe ser el
#último ingresado.

from time import sleep
# from pilas_colas import Pila

class Pila():
    # constructor
    def __init__(self):
        self.lista = []

    #metodos
    def apilar(self,item,info):
        self.lista.append(item)
        if info: print(f"\nElemento {item} apilado, lista actualizada: {self.lista}")

    def mi_pila(self):
        for apilado in reversed(self.lista):
            print(f"[\t {apilado}   \t]")

    def desapilar(self,info):

        if info:
            if self.vacia(): print("\nNo se puede desapilar la lista esta vacia")
            else: print(f"\nElemento {self.lista.pop()} desapilado, lista actualizada: {self.lista}")

        if not self.vacia(): return self.lista.pop()

    def tamanio(self):
        print(f"\nLa pila tiene {len(self.lista)} elementos")

    def vacia(self):
        if len(self.lista) == 0: return True; return False

    def limpiar(self,info):
        self.lista.clear()
        if info: print("\nLista vaciada")
#########################################################

mi_pila_de_nombres = Pila() ## instanciando el objeto

## variables de control
menu_txt = "MENU: \n\t(1) ingresar nombres \n\t(2) desapilar nombres \n\t(3) salir\n\t tu opcion: "
barrera_txt = "*"*15+"\n"
mensaje_de_salida = "SALIENDO DEL PROGRAMA\n"

## proceso
while True:
    try:
        menu = int(input(menu_txt))
    except ValueError: print("\nERROR: solo numeros, intenta denuevo!!");print(barrera_txt);continue
    match menu:
        case 1:
            while True:
                print("precione solo (ENTER) para salir")
                nombre_ingresado = input("ingresa un nombre: ").capitalize()

                if nombre_ingresado == "": break

                mi_pila_de_nombres.apilar(nombre_ingresado,False)

                print(barrera_txt)
                mi_pila_de_nombres.mi_pila()
        case 2:
            if mi_pila_de_nombres.vacia(): print("\n\nla cola ya esta vacia.\n\n"); continue
            mi_pila_de_nombres.desapilar(False)

            print(barrera_txt)

            mi_pila_de_nombres.mi_pila()
            sleep(0.5) ## pequeña pausa
        case 3:
            print()
            print(barrera_txt)
            print(mensaje_de_salida)
            print(barrera_txt)
            break
        case _:
            print("ingrese una opcion valida")