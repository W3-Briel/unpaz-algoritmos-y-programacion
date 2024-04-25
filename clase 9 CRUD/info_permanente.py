# alumno: Angel Gabriel Saucedo
# Algoritmos y Programacion - B1
import pickle as p

class Persona:
    def __init__(self,nombre,genero,edad):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad
        print("se ha creado una persona nueva con el nombre de ",self.nombre)
    
    def __str__(self):
        return f"{self.nombre} {self.genero} {self.edad}"

class ListaPersonas:
    def __init__(self):
        self.personas = []
        listaPersonas = open("ficheroExterno","ab+")
        listaPersonas.seek(0)

        try:
            self.personas = p.load(listaPersonas)
            print(f"se cargaron {len(self.personas)} personas del fichero externo")
        except: print("el archivo esta vacio")
        finally: listaPersonas.close(); del (listaPersonas)

    def guardarPersonasEnFficheroExterno(self):
        listaDePersonas = open("ficheroExterno", "wb")
        p.dump(self.personas, listaDePersonas)
        listaDePersonas.close()
        del(listaDePersonas)

    def get_personas(self):
        for persona in self.personas: print(persona)
    def get_informacionDelFicheroExterno(self):
        print("La informacion del fichero externo es la siguiente: ")
        for p in self.personas: print(p)

    def set_personas(self,datos):
        self.personas.append(datos)
        self.guardarPersonasEnFficheroExterno()
    

instacia_mi_lista = ListaPersonas()

instancia_persona = Persona("Sandra","Femenino",29)
instacia_mi_lista.set_personas(instancia_persona)

instancia_persona = Persona("Sandri","Femenino",23)
instacia_mi_lista.set_personas(instancia_persona)

instancia_persona = Persona("Sandre","Masculino",30)
instacia_mi_lista.set_personas(instancia_persona)

instancia_persona = Persona("Sandru","Masculino",40)
instacia_mi_lista.set_personas(instancia_persona)

# instacia_mi_lista.get_personas()
instacia_mi_lista.get_informacionDelFicheroExterno()