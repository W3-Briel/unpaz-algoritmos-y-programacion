import io

# frase = "hola como estas, a alvaro no le anda la pc"

# datos = open("mi_archivo.txt","w")

# datos.write(frase)
# datos.write("\nEsta linea va abajo")

# datos = open("mi_archivo.txt","r")
# contenido = datos.read()
# print(contenido)

## .readlines() imprime el contenido como si fuera una lista
# datos = open("mi_archivo.txt","r")
# lista = datos.readlines()

# print(lista)
# for i in lista:
#     print(i.strip("\n"))

# datos = open("mi_archivo.txt","a")
# agregar = datos.write("\nseguimos agregando texto al archivo")

# datos.close()

#===================================#

# arch = open("otroarchivo.txt","w")
# arch.write("estoy creando un nuevo archivo")
# arch.close()

# arch = open("otroarchivo.txt","r")
# print(arch.readlines())
# arch.close()

# arch = open("otroarchivo.txt","r")
# arch.seek(17)
# print(arch.readline())
# arch.close()
#===================================#


arch = open("modif_archivo.txt","w")
arch.write("Linea 1 esta es la primer linea")
arch.write("\nLinea 3 esta es la tercer linea")
arch.write("\nLinea 2 esta es la segunda linea")
arch.close()

arch = open("modif_archivo.txt","r+")
lineas = arch.readlines()

lineas[1] = "Linea 2 esta es la segunda linea"
lineas[2] = "\nLinea 3 esta es la tercer linea"

arch.seek(0)
arch.writelines(lineas)
arch.close()

arch = open("modif_archivo.txt","r")
print(arch.read())
arch.close()