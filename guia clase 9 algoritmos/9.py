# alumno: Angel Gabriel Saucedo
# Algoritmos y Programacion - B1
##########################
# Titulo: Carga de personas 1
# Crear un archivo csv llamado personas que contendrá una lista de personas con los siguientes
# campos:
# - cod
# - nombre
# - apellido
# - Dni
# Generar un menú con las opciones
# 1. Cargar Persona
# 2. Listar Persona
# 3. Salir del programa
# Siempre que entre a la opción 1 deberá mostrar todos los usuarios cargados en el archivo.
import csv as c
from module import _functions as f

class Persona():
    def __init__(self,nombre,apellido,dni):
        try:
            self.nombre = str(nombre).capitalize()
            self.apellido = str(apellido).capitalize()
            self.dni = int(dni)
            self.codigo = None
        except ValueError:
            print("los valores para los parametros deberian ser:\ncodigo y dni -> int, nombre y apellido -> str")

    def set_codigo(self,codigo):
        self.codigo = codigo

    def get_persona(self):
        return [self.codigo,
                self.nombre,
                self.apellido,
                self.dni
                ]


class CargarPersona():
    def __init__ (self):
        self.lista = []
        self.archivo = "personas.csv"

    def nombre_del_archivo(self):
        return self.archivo
    def cambiar_archivo(self,nombre):
        self.archivo = nombre+".csv"

    def crear_archivo(self):
        with open(self.archivo,"w", newline="\n") as arch_csv:
            writer = c.writer(arch_csv, delimiter=";")
            writer.writerow(["CODIGO","NOMBRE","APELLIDO","DNI"])
        del arch_csv

    def controlar_datos(self):
        while True:
                while True:
                    nombre = input("nombre: ")
                    if len(nombre) == 0: print("ingresa un nombre porfavor!!"); continue
                    elif len(nombre) > 20: print("maximo 20 caracteres en nombres!"); continue
                    break

                while True:
                    apellido = input("apellido: ")
                    if len(apellido) == 0: print("ingresa un apellido porfavor!!"); continue
                    elif len(apellido) > 20: print("maximo 20 caracteres en apellidos!"); continue
                    break

                while True:
                    try:
                        dni = int(input("dni de la persona: "))
                        if dni > 0:
                            if len(str(dni)) == 0: print("ingrese un dni porfavor!!"); continue
                            elif len(str(dni)) > 15: print("maximo 15 digitos en DNI"); continue
                        else: print("creo que no existen los dni con negativos, intenta denuevo!")
                        break
                    except ValueError:
                        print("ERROR - EL DNI A CARGAR DEBERIA SER UN NUMERO\nIntenta nuevamente!!")
                        continue
                break
        return [nombre,apellido,dni]

    def cargar_personas(self):
        cantidad = f.numeroIterable("cuantas personas quieres agregar?: ")
        contador = 0
        while contador < cantidad:
            print(f"persona {contador+1}")

            informacion = self.controlar_datos()
            persona = Persona(informacion[0],informacion[1],informacion[2])

            self.lista.append(persona); contador+=1

        with open(self.archivo,"a+",newline="\n") as archivo_csv:
            writer = c.writer(archivo_csv,delimiter=";")
            for persona in self.lista:
                archivo_csv.seek(0)
                persona.set_codigo(len(archivo_csv.readlines()))
                writer.writerow(persona.get_persona())
        del archivo_csv

        self.lista = []

class listarDesdeArchivo():
    def __init__(self,archivo):
        self.archivo = archivo

    def mostrar(self):
        try:
            with open(self.archivo,"r",encoding="utf-8") as archivo:
                if len(archivo.readlines()) < 2: return print("el archivo esta vacio.")

                archivo.seek(0)
                for row in archivo:
                    colums = row.replace("\n","").split(";")
                    print(f"{colums[0]:^5} {colums[1]:^20} {colums[2]:^20} {colums[3]:^10}")
        except: print("ERROR - NO SE ENCUENTRA EL ARCHIVO")

def main():
    bbdd = CargarPersona()
    bbdd.crear_archivo()
    while True:

        seleccion = input("<- menu ->\n1. Cargar Persona\n2. Listar Persona\n3. Salir del programa\nelige una opcion: ")
        match seleccion:
            case "1":
                bbdd.cargar_personas()
            case "2":
                archivo = listarDesdeArchivo(bbdd.nombre_del_archivo())
                archivo.mostrar()
            case _: print("\nsaliendo el programa\n"); break

main()

#  Laboratorio de testeo
# ● Ejecute el programa y seleccione la opción 1, cargue 5 personas y vuelva al menú
# principal.
# ● Ingrese a la opción 2 liste todas las personas del archivos.
# ● Seleccione la opción 1, cargue 2 personas y vuelva al menú principal.
# ● Repita punto 2
# ● Salga del programa.