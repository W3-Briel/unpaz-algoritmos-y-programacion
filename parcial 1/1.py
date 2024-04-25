# Ejercicio 1:

# El banco propio de la universidad " BUNPAZ " abre a las 10 AM y otorga 10 turnos desde el número 0 al 9 todos los días. El banco posee 3 cajas A, B y C para atender estos clientes.

# Ud. debe realizar un programa que otorgue los números a cada cliente, estos esperan ser llamados, por las cajas = ['A','B','C']. Las cajas son asignadas aleatoriamente hasta terminar de atender a todos los clientes.
# Recuerde incorporar la siguiente línea: cajas = ['A','B','C']

# Se le otorgarán los TDA correspondientes de Pila y Cola, estarán en un archivo llamado tda_parcial.py este debe alojarse en la misma carpeta donde está ejecutando su programa.
# Recuerde la forma de importar clases desde otro archivo abra su archivo y en la primer línea escriba:  from tda_parcial import * 

from random import choice
from tda_parcial import *

cajas = ["A","B","C"]
bunpaz_turnos = Cola()

print("Turnos\n")
for turno in range(10):
    bunpaz_turnos.encolar(turno)
    print(f"Turno {turno} otorgado")

print("\nSistema de Atencion al cliente\n")

for atendido in range(bunpaz_turnos.largo()):
    print(f"Numero {atendido} Caja {choice(cajas)}")