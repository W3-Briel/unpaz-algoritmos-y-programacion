# alumno: Angel Gabriel Saucedo
# Algoritmos y Programacion - B1
###################################################
class Cola():
    #constructor
    def __init__(self):
        self.heroes = []

    #metodos
    def encolar(self,x):
        self.heroes.append(x)

    def buscar(self):
        buscar= input("Ingrese el nombre de un heroe: ").capitalize()
        for personajes in superheroes.heroes:
            if buscar == personajes[1]:
                return print(f"El personaje buscado es: {personajes[1]}\t el actor es: {personajes[0]}")
        return print("El personaje no existe")

    def es_vacia(self):
        return self.heroes == []

    def desencolar(self,info):
        if info:
            mensaje = "la cola esta vacia, no hay mas heroes" if self.es_vacia() else f"\nHeroes {self.heroes.pop(0)}  (desencolado), cola actualizada: {self.heroes}"
            return mensaje

        if not self.es_vacia(): return self.heroes.pop(0)
superheroes = Cola()
personajes = [('Tony Stark', 'Iron Man'), ('Steve Rogers', 'Capitán América'), ('Natasha Romanoff',
'Black Widow'), ('Bruce Banner', 'Hulk'), ('Thor Odinson', 'Thor'), ('Clint Barton', 'Hawkeye'), ('Wanda Maximoff', 'Scarlet Witch'), ('Vision', 'Vision'), ('Peter Parker', 'Spider-Man'), ('Carol Danvers', 'CapitanaMarvel'), ('Nick Fury', 'Nick Fury'), ('Loki Laufeyson', 'Loki'), ('Phil Coulson', 'Phil Coulson'), ('Maria Hill','Maria Hill'), ('James Rhodes', 'War Machine'), ('Sam Wilson', 'Falcon'), ('Peggy Carter', 'PeggyCarter'), ('Bucky Barnes', 'Winter Soldier'), ('Thanos', 'Thanos'), ('Gamora', 'Gamora'), ('Nebula','Nebula'), ('Drax el Destructor', 'Drax el Destructor'), ('Groot', 'Groot'), ('Rocket Raccoon', 'RocketRaccoon'), ('Peter Quill', 'Star-Lord')] 
print("Personajes  \t    actores")

for i in personajes:
    print(f"{str(i[1]): ^19} {str(i[0])}")
    superheroes.encolar(i)
superheroes.buscar()

for i in range(10):
    print("desencolados",superheroes.desencolar(False))
print("el ultimo personaje encolado es: ",superheroes.heroes[-1])

pj = input("Ingerse el nombre del personaje: ")
actor = input("Ingerse el nombre del actor: ")
personaje_new =(pj,actor)
superheroes.encolar(personaje_new)

print("el ultimo personaje encolado es: ",superheroes.heroes[-1])