# alumno: Angel Gabriel Saucedo
# Algoritmos y Programacion - B1
###################################################
# from pilas_colas import Pila
from random import randint
from time import sleep

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

#############################################################
juego = Pila()

## VARIABLES DE CONTROL
SEGUNDOS = 6
LARGO_DE_LA_PILA = 5
TURNOS_MAXIMOS = LARGO_DE_LA_PILA+2

ganador_txt = "💰wtf que buena memoria!!, TE PASASTE EL JUEGO."
perdedor_txt = "perdiste, bueno intentalo la proxima"
numero_incorrecto_txt = "\n\n😥❌ ERRASTE PRESTA MAS ATENCION!! ❌😥\n"
barrera_txt = "*"*10

## PROCESOS
for i in range(LARGO_DE_LA_PILA):
    numero_aleatorio = randint(10,99)
    juego.apilar(numero_aleatorio,False)

juego.mi_pila()

for segundo in range(SEGUNDOS,0,-1):
    print(f"TIENES {segundo} SEGUNDOS!!", end="\r")
    sleep(1)

print("")

for i in range(100):
    print()

turnos_usados = 1
turnos_errados = 0

while turnos_usados <= TURNOS_MAXIMOS:
    print(barrera_txt)
    print(f"\nTURNO {turnos_usados} DE {TURNOS_MAXIMOS}\n")
    try:
        mi_numero = int(input("🐒 QUE NUMERO DESAPILAMOS??: "))
    except ValueError: print("\n\nSOLO ERAN NUEMEROS!!, te dejo intentar denuevo 🙄🙄\n\n"); continue

    if juego.lista[-1] == mi_numero:
        juego.desapilar(False)

        print(f"⚜ BIEN ERA EL {mi_numero} ✅!!")

        if len(juego.lista) == 0:
            for i in range(3):
                print("\n\nOMG lol XD!!!")
                print(barrera_txt)

            print(ganador_txt); break
        else: print("\n\n|💤|te faltan: ",len(juego.lista))

        turnos_usados+=1
    else:
        if turnos_errados+1 > 2: print(perdedor_txt);break
        print(numero_incorrecto_txt); turnos_usados+=1; turnos_errados+=1