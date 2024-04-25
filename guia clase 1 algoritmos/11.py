# alumno: Angel Gabriel Saucedo
# Algoritmos y Programacion - B1

############ ESTRUCTURAS DE DECISION SIMPLE IF ############

##11 Escribir un programa que permita el ingreso por teclado de una oración de cinco palabras, y
## muestre por pantalla, en minúsculas, en mayúsculas y por último solo el primer carácter de la
## oración en mayúscula.

while True:
    oracion_cinco_palabras = input("escribe cinco palabras: ")
    if len(oracion_cinco_palabras.split(" ")) == 5:
        print("lower; ",oracion_cinco_palabras.lower(),"\n",
              "upper; ",oracion_cinco_palabras.upper(),"\n",
              "capitalize; ",oracion_cinco_palabras.capitalize())
        break
    else:
        print("escribe exactamente 5 palabras..."); continue