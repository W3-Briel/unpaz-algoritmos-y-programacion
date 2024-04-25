# alumno: Angel Gabriel Saucedo
# Algoritmos y Programacion - B1

############ ENTRADAS INPUT() ############

##6 Escribir un programa que pregunte al usuario por el número de horas trabajadas y el costo por
## hora. Después debe mostrar por pantalla la paga que le corresponde. 

horas_trabajadas = float(input("Cuantas horas has trabajado?: "))
paga_por_hora = float(input("Cual es la paga por hora?: "))
pago_correspondiente = horas_trabajadas * paga_por_hora
print(
    "Cobrando ${} por hora, al haber trabajado {} hrs te corresponde ${}"
    .format(paga_por_hora,horas_trabajadas,pago_correspondiente)) # salida con formato