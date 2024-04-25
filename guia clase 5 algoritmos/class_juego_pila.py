# alumno: Angel Gabriel Saucedo
# Algoritmos y Programacion - B1
###################################################
from pilas_colas import Pila
from random import randint
from time import sleep

class Juego_pila(Pila):
    def __init__(self,largo_de_la_pila,segundos_para_memorizar,fallos_permitidos):
        super().__init__() # Pila.__init__(self)

        self.segundos = int(segundos_para_memorizar)
        self.largo_de_la_pila = int(largo_de_la_pila)
        self.fallos_permitidos = int(fallos_permitidos)
        self.turnos_maximos = int(largo_de_la_pila) + int(fallos_permitidos)

        self.ganador_txt = "💰wtf que buena memoria!!, TE PASASTE EL JUEGO."
        self.perdedor_txt = "perdiste, bueno intentalo la proxima"
        self.numero_incorrecto_txt = "\n\n😥❌ ERRASTE PRESTA MAS ATENCION!! ❌😥\n"
        self.barrera_txt = "*"*10

        ## se supone que son atributos privados eh
        self.__maximo_valor_aleatorio = 99
        self.__minimo_valor_aleatorio = 10
        self.__turnos_usados = 1
        self.__turnos_errados = 0
        self.__totales_ganadas = 0
        self.__totales_perdidas = 0
        self.__menu_confirmar = "si desea confirmar (1), cancelar (2): "

    ##metodos funcionales
    def __cargar_datos(self):
        for i in range(self.largo_de_la_pila):
            self.apilar(randint(self.__minimo_valor_aleatorio,self.__maximo_valor_aleatorio),False)

    def __mostrar_tiempo(self,segundos):
        for segundo in range(segundos,0,-1):
            print(f"TIENES {segundo} SEGUNDOS!!", end="\r")
            sleep(1)
        print("")

    def __limpiar_consola(self):
        for i in range(100):
            print()

    def __resetear_juego(self):
        self.__turnos_errados = 0
        self.__turnos_usados = 1
        self.limpiar(False)

    ## main
    def iniciar_juego(self,rondas,segundos_entre_rondas):
        for ronda in range(rondas):
            print(self.barrera_txt)
            print(F"\nRONDA {ronda+1}")
            print(self.barrera_txt)

            self.__cargar_datos()
            self.mi_pila()
            self.__mostrar_tiempo(self.segundos)
            self.__limpiar_consola()

            while self.__turnos_errados <= self.turnos_maximos:
                print(self.barrera_txt)
                print(f"\nTURNO {self.__turnos_usados} DE {self.turnos_maximos}\n")
                try:
                    mi_numero = int(input("🐒 QUE NUMERO DESAPILAMOS??: "))
                except ValueError: print("\n\nSOLO ERAN NUEMEROS!!, te dejo intentar denuevo 🙄🙄\n\n"); continue
                if self.lista[-1] == mi_numero: 
                    self.desapilar(False)
                    print(f"⚜ BIEN ERA EL {mi_numero} ✅!!")

                    if len(self.lista) == 0:
                        for i in range(3):
                            print("\n\nOMG lol XD!!!")
                            print(self.barrera_txt)
                        self.__limpiar_consola()
                        print(self.ganador_txt)
                        self.__totales_ganadas+=1; break

                    else: print("\n\n|💤|te faltan: ",len(self.lista))

                    self.__turnos_usados +=1
                else: 
                    if self.__turnos_errados+1 > self.fallos_permitidos:
                        self.__limpiar_consola()
                        print(self.perdedor_txt)
                        self.__totales_perdidas+=1;break
                    print(self.numero_incorrecto_txt); self.__turnos_usados+=1; self.__turnos_errados+=1

            self.__resetear_juego()
            print(self.barrera_txt)

            if ronda == rondas-1: break
            self.__mostrar_tiempo(segundos_entre_rondas)

        print("GRACIAS POR JUGAR.\nEN TOTAL;")
        print(f"\tGANASTE {self.__totales_ganadas} Y PERDISTE {self.__totales_perdidas}")

    ## personalizar mensajes
    def personalizar_ganador_txt(self):
        print("el mensaje que estas intetando remplazar es:\n")
        print(self.ganador_txt)
        nueva_configuracion = input("por cual mensaje deseas remplazarlo?: ")
        while True:
            confirmar = input(self.__menu_confirmar)
            match confirmar:
                case "1":
                    self.ganador_txt = nueva_configuracion
                    print("cambios realizados con exito."); break
                case "2":
                    print("personalizacion cancelada."); break
                case _:
                    print("ERROR; solo ingrese lo solicitado.")

    def personalizar_perdedor_txt(self):
        print("el mensaje que estas intetando remplazar es:\n")
        print(self.perdedor_txt)
        nueva_configuracion = input("por cual mensaje deseas remplazarlo?: ")
        while True:
            confirmar = input(self.__menu_confirmar)
            match confirmar:
                case "1":
                    self.perdedor_txt = nueva_configuracion
                    print("cambios realizados con exito."); break
                case "2":
                    print("personalizacion cancelada."); break
                case _:
                    print("ERROR; solo ingrese lo solicitado.")

    def personalizar_numero_incorrecto_txt(self):
        print("el mensaje que estas intetando remplazar es:\n")
        print(self.numero_incorrecto_txt)
        nueva_configuracion = input("por cual mensaje deseas remplazarlo?: ")
        while True:
            confirmar = input(self.__menu_confirmar)
            match confirmar:
                case "1":
                    self.numero_incorrecto_txt = nueva_configuracion
                    print("cambios realizados con exito."); break
                case "2":
                    print("personalizacion cancelada."); break
                case _:
                    print("ERROR; solo ingrese lo solicitado.")

    def personalizar_barrera_txt(self):
        print("el mensaje que estas intetando remplazar es:\n")
        print(self.barrera_txt)
        nueva_configuracion = input("por cual mensaje deseas remplazarlo?: ")
        while True:
            confirmar = input(self.__menu_confirmar)
            match confirmar:
                case "1":
                    self.barrera_txt = nueva_configuracion
                    print("cambios realizados con exito."); break
                case "2":
                    print("personalizacion cancelada."); break
                case _:
                    print("ERROR; solo ingrese lo solicitado.")

    def personalizar_valor_minimo_aleatorio(self):
        print("el valor minimo aleatorio actualmente es; ",self.__minimo_valor_aleatorio)
        while True:
            try:
                nueva_configuracion = int(input("cual valor minimo deseas?: ")); break
            except ValueError: print("ERROR; solo nuemeros.")

        while True:
            confirmar = input(self.__menu_confirmar)
            match confirmar:
                case "1":
                    self.__minimo_valor_aleatorio = nueva_configuracion
                    print("cambios realizados con exito."); break
                case "2":
                    print("personalizacion cancelada."); break
                case _:
                    print("ERROR; solo ingrese lo solicitado.")

    def personalizar_valor_maximo_aleatorio(self):
        print("el valor maximo aleatorio actualmente es; ",self.__maximo_valor_aleatorio)
        while True:
            try:
                nueva_configuracion = int(input("cual valor minimo deseas?: ")); break
            except ValueError: print("ERROR; solo nuemeros.")

        while True:
            confirmar = input(self.__menu_confirmar)
            match confirmar:
                case "1":
                    self.__maximo_valor_aleatorio = nueva_configuracion
                    print("cambios realizados con exito."); break
                case "2":
                    print("personalizacion cancelada."); break
                case _:
                    print("ERROR; solo ingrese lo solicitado.")

    ## informacion;
    def mostrar_informacion(self):
        print("** CARACTERISTICAS PERMANENTES(al instanciar) **")
        print(f"\tlos segundos de juego son; {self.segundos}")
        print(f"\tel largo de la pila; {self.largo_de_la_pila}")
        print(f"\tlos fallos permitod son; {self.fallos_permitidos}")
        print(f"\tlos turnos maximos son; {self.turnos_maximos}")
        print("\n\n")
        print("** CARACTERISTICAS PERSONALIZABLES **")
        print("Texto ganador_txt:\n");print("\t",self.ganador_txt)
        print("Texto perdedor_txt:\n");print("\t",self.perdedor_txt)
        print("Texto numero_incorecto_txt:\n");print("\t",self.numero_incorrecto_txt)
        print("Texto barrera.txt:\n");print("\t",self.barrera_txt)
        print()
        print(f"Valor minimo aleatorio:\t{self.__minimo_valor_aleatorio}")
        print(f"Valor maximo aleatorio:\t{self.__maximo_valor_aleatorio}")

#### tengo que mejorar el sistema de personalizacion pero bue

jueguito = Juego_pila(5,5,2)
jueguito.iniciar_juego(3,3)