# alumno: Angel Gabriel Saucedo
# Algoritmos y Programacion - B1
####################################
# Realice un código, donde MiArchivo sea un TDA que tiene dos métodos: escribir y leer. El
# método escribir abre el archivo en modo de escritura (“w”) y escribe el texto proporcionado.
# El método leer abre el archivo en modo de lectura (“r”) y devuelve el contenido del archivo.
# Tenga en cuenta que este código sobrescribirá cualquier contenido existente en el archivo
# cuando se use el método escribir.
# ¿Cómo agregaría el texto al final del archivo sin eliminar el contenido existente?

class MiArchivo():
    def __init__(self,nombre,extencion):
        self.nombre = nombre
        self.extencion = extencion
        self.formato = f"{self.nombre}.{self.extencion}"
    
    def escritura(self):
        texto = input("que texto quieres escribir en el archivo??: ")
        with open(self.formato,"w", encoding="utf-8") as archivo:
            archivo.write(texto)

    def leer(self):
        try:
            with open(self.formato,"r", encoding="utf-8") as archivo:
                print(archivo.read())
        except: print("ERROR, no se encuentra el archivo creado")

    def agregar(self):
        with open(self.formato,"a", encoding="utf-8") as archivo:
            texto = input("que texto quieres agregar??: ")
            archivo.write(texto)

instancia = MiArchivo("mono","txt")

# instancia.escritura()
# instancia.leer()
# instancia.agregar()