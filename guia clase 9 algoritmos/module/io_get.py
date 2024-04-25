# alumno: Angel Gabriel Saucedo
# Algoritmos y Programacion - B1
##########################

def parseInfo(file):
    isCorrectFormat = "<class '_io.TextIOWrapper'>"
    if isCorrectFormat == str(type(file)):
        parset = file.__str__().split(" ")
        return f"{parset[1]}\n{parset[2]}\n{parset[3][:-1]}"
    return "this function(parseInfo) error is in 'module/io_get.py'."

def tablaN(tabla):
    temporal = []
    try:
        for multiplo in range(1,11):
            resultado = int(tabla) * multiplo
            formato = f"{int(tabla)} X {multiplo} = {resultado}\n"
            
            if multiplo == 10: formato = formato[:-2]
            temporal.append(formato)

        with open(f"tabla-{int(tabla)}.txt", "w+", encoding="utf-8") as file:
            file.writelines(temporal)
        del file
    except ValueError:
        print("this function(tablaN) error is in 'module/io_get.py'.",ValueError)

def busquedaTextual(archivo,text,sensible):
    coincidencias = []
    try:
        with open(archivo,"r",encoding="utf-8") as file:
            for numeroDeLinea,contenidoDeLinea in enumerate(file.readlines()):

                if (str(text).lower() in contenidoDeLinea.lower()) and sensible:
                    coincidencias.append([numeroDeLinea,contenidoDeLinea[:-1]])
                    continue

                if str(text) in contenidoDeLinea:
                    coincidencias.append([numeroDeLinea,contenidoDeLinea[:-1]])
        del file
    except:
        print("this function(busquedaTextual) error is in 'module/io_get.py'.")
    finally: return coincidencias

def editarArchivo(nombreDelArchivo,buscar,remplazar,sensible):
    try:
        with open(nombreDelArchivo,"r",encoding="utf-8") as file:
            print(file.read()); file.seek(0)
            lineas = file.readlines()
            coincidencias = busquedaTextual(nombreDelArchivo,str(buscar),bool(sensible))
            if len(coincidencias) > 0:
                for indice,editar in enumerate(coincidencias):
                    coincidencias[indice] = [editar[0],editar[1].replace(str(buscar),str(remplazar))]
                for lineaEditada in coincidencias:
                    lineas[lineaEditada[0]] = lineaEditada[1]+"\n"
                with open(nombreDelArchivo,"w+",encoding="utf-8") as fileEdit:
                    fileEdit.writelines(lineas)
                    fileEdit.seek(0)
            else: print("no se encontraron coincidencias")
    except ValueError:
        print("this function(editarArchivo) error is in 'module/io_get.py'.",ValueError)
    except: print("this function(editarArchivo) error is in 'module/io_get.py'.")