# alumno: Angel Gabriel Saucedo
# Algoritmos y Programacion - B1

############ ESTRUCTURAS ITERATIVAS FOR ############

##21 Escribir un programa que enumere los nombres de la lista 
## nombres = ['Jose' ,'Pedro' ,'Armando', 'Analía','Florencia'] . utilice la función enumerate 

nombres = ['Jose' ,'Pedro' ,'Armando', 'Analía','Florencia']

for indice, nombre in enumerate(nombres): print(indice+1, nombre)