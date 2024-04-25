# alumno: Angel Gabriel Saucedo
# Algoritmos y Programacion - B1
##################################################
#Desarrollar un programa que cargue los datos de un triángulo. Implementar una clase con los
#métodos para inicializar los atributos, imprimir el valor del lado con un tamaño mayor y el tipo
#de triángulo que es (equilátero, isósceles o escaleno).

import time as t
class Trianguo():
    #inicializamos
    def __init__(self):
        while True:
            try:
                self.lado1=int(input("ingrese el valor del primer lado: "))
                self.lado2=int(input("ingrese el valor del segundo lado: "))
                self.lado3=int(input("ingrese el valor del tercer lado: "))
                break
            except ValueError: print("ERROR al instanciar el objeto, verifica los argumentos dados!!")
        self.all_equals = self.lado1 == self.lado2 and self.lado2 == self.lado3
        self.two_equals = self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3

    #metodos
    # imprimir lados
    def imprimir_lados(self):
        print("los lados del triangulo tiene el valor de")
        print("Lado 1: ", self.lado1)
        print("Lado 2: ", self.lado2)
        print("Lado 3: ", self.lado3)

    # comprobamos el lado mayor
    def lado_mayor(self):
        if self.all_equals: return print("todos los lados son iguales")
        elif self.lado1 == self.lado2: print("los lados mayores son","Lado 1: ",self.lado1,"\nLado 2: ",self.lado2)
        elif self.lado2 == self.lado3: print("los lados mayores son","Lado 2: ",self.lado2,"\nLado 3: ",self.lado3)
        elif self.lado1 == self.lado3: print("los lados mayores son","Lado 1: ",self.lado1,"\nLado 3: ",self.lado3)
        else:
            print("el lado mayor es ")
            if (self.lado1 > self.lado2) & (self.lado1 > self.lado3):
                print("Lado 1: ",self.lado1)
            elif self.lado2 > self.lado3:
                print("Lado 2: ", self.lado2)
            else: print("Lado 3: ", self.lado3)

    # tipo del triangulo
    def tipo_de_triangulo(self):
        
        if self.all_equals: print("es un triangulo equilatero")
        elif self.two_equals: print("es un triangulo isosceles")
        else: print("es un triangulo escaleno")
        
        
triangulo = Trianguo()
triangulo.imprimir_lados()
triangulo.lado_mayor()
triangulo.tipo_de_triangulo()