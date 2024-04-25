# alumno: Angel Gabriel Saucedo
# Algoritmos y Programacion - B1
##################################################
# Realizar un programa que tenga una clase Persona con las siguientes características. La clase 
# tendrá como atributos el nombre y la edad de una persona. Implementar los métodos 
# necesarios para inicializar los atributos utilizando el constructor (__init__), mostrar los datos e 
# indicar si la persona es mayor de edad o no. 
# ¡Utilice el constructor!

class Persona():
    def __init__(self):
        self.nombre = input("ingresa tu nombre: ").capitalize()
        self.edad = input("ingresa tu edad: ")
    
    #metodos
    def is_of_legal_age(self):
        try:
            if int(self.edad) >= 18:
                print(self.nombre," es mayor de edad, tiene",self.edad," años.")
                return True
            else: print(self.nombre," es menor de edad, tiene",self.edad," años."); return False
        except ValueError:
            print("ERROR al instanciar el objeto, verifica los argumentos!!")

yo = Persona()
yo.is_of_legal_age()