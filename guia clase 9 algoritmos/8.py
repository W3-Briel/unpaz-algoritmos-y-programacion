# alumno: Angel Gabriel Saucedo
# Algoritmos y Programacion - B1
##########################
# Título: Reemplazar texto
# Escriba un programa que abra un archivo de texto, el nombre debe ser solicitado el usuario
# este debe tener la característica de ser un archivo de texto plano ej: cancion2.txt
# ● Investigue qué función de python reemplaza textos.
# ● Muestre todo el texto en pantalla
# ● Solicite al usuario un texto a buscar y el texto que reemplaza al texto buscado.
# ● Analice el archivo, busque y encuentre dentro del archivo el texto buscado
# ● y reemplácelo por el texto de reemplazo.
# ● Atención, el texto buscado es "sensible" a mayusculas o minusculas.
# ● Trate de solucionar cómo guardar los cambios, revise el material visto en clases.
# ● Si no hubiera coincidencia deberá avisar.
# Atención cuando abra el archivo utilice la codificación utf8
# with open(nombre_archivo,'r',encoding='utf8') as xxxx
from module import io_get

NOMBRE_DE_ARCHIVO = "cancion2.txt"

def editarArchivo(nombreDelArchivo):
    try:
        with open(nombreDelArchivo,"r",encoding="utf-8") as file:
            # mostramos el texto
            print(file.read()); file.seek(0)
            lineas = file.readlines()
            BUSCAR = input("intruduce el texto a buscar: ")
            coincidencias = io_get.busquedaTextual(nombreDelArchivo,BUSCAR,False)

            if len(coincidencias) > 0:
                REMPLAZAR = input("por cual otro deseas remplazar las coincidencias?: ")
                for indice,editar in enumerate(coincidencias):
                    coincidencias[indice] = [editar[0],editar[1].replace(BUSCAR,REMPLAZAR)]

                ## remplazamos las lineas originales con las lineas editadas.
                for lineaEditada in coincidencias:
                    lineas[lineaEditada[0]] = lineaEditada[1]+"\n"

                ## re escribimos el archivo con las lineas editadas
                with open(nombreDelArchivo,"w+",encoding="utf-8") as fileEdit:
                    fileEdit.writelines(lineas); fileEdit.seek(0)
                    print("*"*30)
                    print(f"despues de editar el texto quedaria asi:\n{fileEdit.read()}")
                    print("*"*30)
                    print(f"se afectaron {len(coincidencias)} lineas")

            else: print("no se encontraron coincidencias")
    except: print("ERROR - revisar los parametros")

editarArchivo(NOMBRE_DE_ARCHIVO)