# alumno: Angel Gabriel Saucedo
# Algoritmos y Programacion - B1
from io import open
# from io import

#creamos y abrimos
archivo_texto = open("archivo.txt","w")
frase = "este es mi texto\nsoy\nnuevo"
#modificamos y escribimos
archivo_texto.write(frase)
archivo_texto.close()

#leemos la informacion
archivo_texto = open("archivo.txt","r")
texto = archivo_texto.read()
# print(texto)

lineas_texto = archivo_texto.readlines()
archivo_texto.close()
# print(type(lineas_texto))

## agregar informacion abajo
archivo_texto = open("archivo.txt","a")
archivo_texto.write("\nsiempre lorem ipsum")
archivo_texto.close()

## mover puntero

archivo_texto = open("archivo.txt","r+")
print(archivo_texto.read())
archivo_texto.seek(0)
# archivo_texto.write("\nmonoasddddd"*100)
print("*"*20,"\n",archivo_texto.read())



# archivo_texto.writelines("manos de monoasfasdfasdddddddddddddaaaaaaaaaaaaa")
# archivo_texto.seek(0)
# print(archivo_texto.read())

archivo_texto.close()