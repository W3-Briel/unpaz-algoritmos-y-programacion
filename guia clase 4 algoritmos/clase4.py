#bidimensional = [[1,2],[3,4],[5,6]]

#for pos, i in  enumerate(bidimensional):
#    for pos1, j in enumerate(i):
#        print(f"| {j} - [{pos}] [{pos1}]", end="")
#    print()

class Persona():
    #inicializamos caracteristicas, atributos
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = int(edad)
    
    #creamos los metodos
    def mayor_o_menor_de_edad(self):
        if self.edad >= 18:
            return "mayor de edad"
        else: return "menor de edad"
    
    def nombre_persona (self):
        return self.nombre
    def que_año_nacio(self,año_actual):
        return año_actual - self.edad

class Alumno():
    nota = 10
    nombre = "angel saucedo"

    #metodos
    def estado_de_la_nota(self):
        if self.nota >= 4:
            return "aprobado"
        else: return "desaprobado"

    def nombre_del_alumno(self):
        return f"el alumno es {self.nombre}"


alumno = Alumno()
print(alumno.estado_de_la_nota(),",", alumno.nombre_del_alumno())

miPersona = Persona("angel","20")
print(f"{miPersona.nombre_persona()} es {miPersona.mayor_o_menor_de_edad()}")
#print(miPersona.que_año_nacio(2023))