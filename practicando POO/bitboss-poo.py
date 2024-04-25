import random as r

class Personaje():
    #no es necesario declarar estos atributos, ya que utilizamos el constructor y al instanciar los pide como argumento.
    # nombre = "Default"
    # fuerza = 0
    # inteligencia = 0
    # defensa = 0
    # vida = 0

    #self es un argumento que hace refencia a si mismo "al objeto", y nos permite atravez de la nomenclatura de punto
    #acceder a los atributos y metodos de la clase.
    def __init__(self,nombre,fuerza,inteligencia,defensa,vida):
        #con __atributo las creamos en privado, significa que desde afuera de la clase no se podran acceder a sus valores
        # o eso pareciera ser. realmente python no tiene contro sobre el acceso, solo los simula. atributos y metodos son publicos.
        
        # solo sirve para orientar a los que leen o utilizan el codigo.
        self.nombre = str(nombre).capitalize()
        self.fuerza = int(fuerza)
        self.inteligencia = int(inteligencia)
        self.defensa = int(defensa)
        self.vida = int(vida)
    
    #METODOS

    def atributos(self):
        print(self.nombre,":")
        print(f"º Fuerza: {self.fuerza}")
        print(f"º Inteligencia: {self.inteligencia}")
        print(f"º Defensa: {self.defensa}")
        print(f"º Vida: {self.vida}")
    
    def subir_nivel(self,fuerza,inteligencia,defensa):
        self.fuerza += fuerza
        self.inteligencia += inteligencia
        self.defensa += defensa

        print("*"*20)
        print("TIENES NUEVOS ATRIBUTOS!!")
        self.atributos()
        print("*"*20)
    
    def esta_vivo(self):
        return self.vida > 0
    
    def morir(self):
        self.vida = 0
        print(self.nombre, "ha muerto")
    
    def daño(self,enemigo):
        return self.fuerza - enemigo.defensa
    
    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida -= daño
        print(f"{self.nombre} ha realizado {daño} puntos de daño a {enemigo.nombre}")
        if enemigo.esta_vivo():
            print(f"la vida de {enemigo.nombre} es {enemigo.vida}")
        else:
            enemigo.morir()
    
    # acceder o modificar atributos con control. se crea un metodo get para leer, y otro metodo set para reasignar
    def get_fuerza(self):
        return self.fuerza
    
    def set_fuerza(self, fuerza):
        if fuerza < 0:
            print("Error, has introduccido un vlaor negativo")
        else:
            self.fuerza = fuerza



############ herencias
# la clase guerrero hereda los metodos de Personaje, pero si queremos agregar atributos a nuestro constructor,
# tenemos que llamar el constructor con todos los atributos de la clase padre con la funcion dentro de nuestro __init__ super().__init__(atributos)
# despues agregamos nuestros atributos.

# los que nos permite la funcion super() es que directamente hace referencia a la clase padre. entonces podemos usar nomenclatura de punto, para utilizar los metodos y caracteristicas.

# tener en cuenta que no puedo editar los atributos "privados" los que tienen "__atributo" desde otra clase.
# o almenos creo que ese era mi error...

class Guerrero(Personaje):
    def __init__(self,nombre,fuerza,inteligencia,defensa,vida,espada):
        super().__init__(nombre,fuerza,inteligencia,defensa,vida)
        self.__espada = espada
    
    #metodos
    def cambiar_arma(self):
        opcion = int(input("Elige un arma: (1) Acero Valyrio, daño 8. (2) Matadragones, daño 10: "))
        if opcion == 1: self.__espada = 8
        elif opcion == 2: self.__espada = 10
        else: print("Numero de arma incorrecto")
    
    # como ya existia el metodo atributos en la clase padre y solo queremos agregar mas codigo, utilizamos "super().atributos()"
    # y agregamos lo que queremos luego
    ## INDEPENDIENTEMENTE de que se llame igual el metodo, cuando llamemos el metodo desde una instancia Guerrero, se estara ejecutando
    ## desde Guerrero, es decir. se sobre escribe el metodo.
    ## en este caso nos servia llamar el metodo atributos de Personaje, ya que es lo mismo, nomas que con un print mas.
    
    def atributos(self):
        super().atributos()
        print(f"º Espada: {self.__espada}")
    
    ## realmente estamos sobreescribiendo el codigo de la clase padre.
    def daño(self,enemigo):
        return (self.fuerza*self.__espada) - enemigo.defensa

class Mago(Personaje):
    def __init__(self,nombre,fuerza,inteligencia,defensa,vida,libro):
        ## NO HACE FALTA AGREGAR EL SELF EN LA FUNCION SUPER()
        # tambien se puede hacer:
        # Personaje.__init__(self,nombre,fuerza,inteligencia,defensa,vida)
        super().__init__(nombre,fuerza,inteligencia,defensa,vida)
        self.__libro = libro
    
    #metodos
    def atributos(self):
        super().atributos()
        print(f"º Libro: {self.__libro}")
    
    def daño(self, enemigo):
        return (self.inteligencia*self.__libro) - enemigo.defensa
    
#nomenclatura de punto "objeto_instanciado.valor_o_metodo"
# print(f"El nombre del jugador es: {miPersonaje.nombre}")
# print(f"La fuerza del jugador es: {miPersonaje.fuerza}")

# miPersonaje.atributos()
# miEnemigo.atributos()

# miPersonaje.subir_nivel(2,3,2)
# miPersonaje.morir()
# print(miPersonaje.esta_vivo())

# print(miPersonaje.daño(miEnemigo))
# mi_personaje.atacar(mi_enemigo)

# print(mi_personaje.get_fuerza())
# mi_personaje.set_fuerza(-1)

################ MANERA DE ACCEDER A METODOS Y ATRIBUTOS "PRIVADOS" EN PYTHON ####################
# mi_personaje._Personajefuerza = -123123
# mi_personaje._Personajemorir()
# mi_personaje.atributos()

mi_personaje = Personaje("briel",10,2,5,100)
yo_guerrero = Guerrero("briel malo",20,10,10,100,5)
mi_enemigo = Mago("universidad",8,10,4,100,6)

# yo_guerrero.atacar(mi_personaje)
# mi_enemigo.atacar(yo_guerrero)

def combate_epico(player1,player2):
    peleadores= [player1,player2]
    turno= 1
    while player1.esta_vivo() and player2.esta_vivo():
        inicia= r.choice(peleadores)
        print("\nTurno", turno)
        if inicia == player1: print(">>> Accion de",player1.nombre); inicia.atacar(player2)
        else: print(">>> Accion de",player2.nombre); inicia.atacar(player1)
        
        turno+= 1
    
    if player1.esta_vivo(): print("\n| Ha ganado", player1.nombre)
    elif player2.esta_vivo(): print("\n| Ha ganado", player2.nombre)
    else: print("\n| Empate")
        
combate_epico(yo_guerrero,mi_enemigo)

# mi_personaje.atributos()
# yo_guerrero.atributos()
# mi_enemigo.atributos()


# yo_guerrero.cambiar_arma()
# yo_guerrero.atributos()