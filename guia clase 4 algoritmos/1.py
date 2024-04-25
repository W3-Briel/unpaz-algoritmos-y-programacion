# alumno: Angel Gabriel Saucedo
# Algoritmos y Programacion - B1

##################################################
# Realizar un programa que conste de una clase llamada Alumno que tenga como atributos el 
# nombre y la nota del alumno. Definir los métodos para inicializar sus atributos, imprimirlos y 
# mostrar un mensaje con el resultado de la nota y si ha aprobado o no. 
# ¡No utilice el constructor!. 

class Alumno():
    nombre  = input("nombre del alumno: ").capitalize()
    nota = input("nota del alumno: ")
    
    def has_aprobed(self):
        try:
            if int(self.nota) > 10: print("la nota debe estar del 1 al 10.")
            elif int(self.nota) >= 4: print(f"el alumno {self.nombre} ha aprobado con {self.nota}"); return True
            else: print(f"el alumno {self.nombre} ha desaprobado con {self.nota}"); return False
        except ValueError:
            print("ERROR al instanciar el objeto, verifica los argumentos!!")

yo_alumno = Alumno()
yo_alumno.has_aprobed()