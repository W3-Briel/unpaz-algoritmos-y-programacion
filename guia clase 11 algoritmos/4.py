# alumno: Angel Gabriel Saucedo
# Algoritmos y Programacion - B1
####################################
# Realice un código que implemente un TDA que defina una clase Coche con métodos:
# guardar_en_archivo y leer_desde_archivo la información del coche en un archivo. El
# método guardar_en_archivo abre el archivo en modo de escritura (“w”) y escribe la
# información del coche en él. El método leer_desde_archivo abre el mismo archivo en modo
# de lectura (“r”) y lee la información del coche desde él. Por último, cree un objeto Coche,
# que guarde en el archivo información sobre un coche en particular y luego lea la misma
# información desde el mismo archivo. 

from pickle import load,dump

class Coche():
    def __init__(self, marca,modelo):
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False
        self.referencia = None
    
    #### setters
    def arrancar(self):
        self.enmarcha = True
    def acelerar (self):
        self.acelera = True
    def frenar(self):
        self.frena = True
    def estado(self):
        print(f"Marca: {self.marca}\nModelo: {self.modelo}\nEn marcha: {self.enmarcha}\nAcelerando: {self.acelera}\nFrenando: {self.frena}")
    #### getters

    def guardar_en_archivo(self,archivo):
        with open(str(archivo),"wb") as file:
            dump(self,file)
            self.referencia = archivo
        del file
    def leer_archivo(self,archivo):
        try:
            with open(str(archivo),"rb") as file:
                self.referencia = archivo
                datos = load(file)

                # transformamos los atributos
                self.marca = datos.marca
                self.modelo = datos.modelo
                self.enmarcha = datos.enmarcha
                self.acelera = datos.acelera
                self.frena = datos.frena
            del file
        except: print("ERROR - no se encuentra el archivo")

instancia1 = Coche("motorola","g42") ## como no se de autos pongo celulares jajasdf
instancia2 = Coche("alcatel","1")

## guardamos la informacion de instancia1 en un archivo binario
instancia1.guardar_en_archivo("instancia1")

## creamos leemos el estado de instancia2
instancia2.estado()
## mutamos la informacion de instancia2 a la informacion de instancia1
instancia2.leer_archivo("instancia1")
## mostramos el estado para que se leer el cambio
instancia2.estado()