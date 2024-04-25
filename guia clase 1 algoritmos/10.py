# alumno: Angel Gabriel Saucedo
# Algoritmos y Programacion - B1

############ CADENAS ############

##10 Escribir un programa que solicite la fecha de nacimiento en formato “dd/mm/aaaa” , y muestre
## por pantalla la fecha por separado el día, el mes y el año.

fecha_dia,fecha_mes,fecha_año = input("escribe tu fecha de nacimiento con el formato 'dd/mm/aaaa': ").split("/")

print("""dia: {}
mes: {}
año: {}""".format(fecha_dia,fecha_mes,fecha_año))