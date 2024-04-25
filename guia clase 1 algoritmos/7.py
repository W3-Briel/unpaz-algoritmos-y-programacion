# alumno: Angel Gabriel Saucedo
# Algoritmos y Programacion - B1

############ ENTRADAS INPUT() ############

##7 Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer
## venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben
## calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada
## payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos
## y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado

PESO_DE_PAYASO_EN_GRAMOS = 122
PESO_DE_MUNECA_EN_GRAMOS = 75 #ñ

envios_payasos,envios_muñecas = int(input("Cuantos payasos van en este envio?: ")),int(input("Cuantas muñecas van en este envio?: "))

peso_total = (PESO_DE_PAYASO_EN_GRAMOS * envios_payasos) + (PESO_DE_MUNECA_EN_GRAMOS * envios_muñecas)

informacion_del_envio = f"el peso total del envio es {peso_total/1000} Klg" if peso_total >= 1000 else f"el peso total del envio es de {peso_total} gramos" # operador ternario

print(informacion_del_envio)

# if peso_total >= 1000:
#     print(f"el peso total del envio es {peso_total/1000} Klg") #salida con formato y operaciones sin concatenar
# else:
#     print("el peso total del envio es de ",peso_total," gramos") #salida compuesta
