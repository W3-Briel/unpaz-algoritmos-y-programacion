# alumno: Angel Gabriel Saucedo
# Algoritmos y Programacion - B1
##################################################
# Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el 
# método __init__. Calcular después la suma, resta, multiplicación y división. Utilizar un método 
# para cada una e imprimir los resultados obtenidos. Llamar a la clase Calculadora.

class Calculadora():
    def __init__(self):
        while True:
            try:
                self.primera_entrada = int(input("Ingresa el primer valor: "))
                self.segunda_entrada = int(input("Ingresa el segundo valor: "))
                break
            except ValueError:
                print("los valores solo pueden ser numeros.")

    #metodos
    def suma(self):
        resultado = int(self.primera_entrada) + int(self.segunda_entrada)
        return print("el resutado es: ",resultado)

    def resta(self):
        resultado = self.primera_entrada - self.segunda_entrada
        return print("el resutado es: ",resultado)

    def multiplicar(self):
        resultado = int(self.primera_entrada) * int(self.segunda_entrada)
        return print("el resutado es: ",resultado)
            
    def dividir(self):
        try:
            resultado = int(self.primera_entrada) / int(self.segunda_entrada)
            return print("el resutado es: ",resultado)
        except ZeroDivisionError:
            print("no se puede dividir entre cero.")

mi_calculadora = Calculadora()
mi_calculadora.dividir()