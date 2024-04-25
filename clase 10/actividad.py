# alumno: Angel Gabriel Saucedo
# Algoritmos y Programacion - B1
import csv
def carga_persona():
    codigo = 0

    #apertura del archivo
    with open("personas.txt","a+", encoding="utf-8",newline="\n") as archivo:
        # vuelvo el puntero a al principio porque a+ abre y se posiciona al final
        archivo.seek(0)
        print("\n Listado de personas \n")
        #generamos el objeto del tipo csv archivo de escritura.
        lectura = csv.reader(archivo, delimiter=";")
        for cod, nombre, apellido, dni in lectura:
            print(f"{cod:<15}{nombre:<25}{apellido:<25}{dni:<10}")
            if cod != "":
                codigo = int(cod)
        #generamos el objeto del tipo csv archivo de escritura.
        escritura = csv.writer(archivo,delimiter=";")
        if codigo == 0:
            escritura.writerow(["CODIGO","NOMBRE","APELLIDO","DNI"])
        print("\n Carga de personas")
        while True:
            nom = input("\nIngrese nombre: ")
            ape = input("\nIngrese apellido: ")
            dni = input("\nIngrese DNI: ")
            if nom != "" and ape != "" and dni != "":
                codigo += 1
                #encierro los datos en una lista
                escritura.writerow([codigo,nom,ape,dni])
                print("Usuario agregado correctamente\n")

                op = input("Desea continuar con la carga de personas > (S)i o (N)o").upper()
                if op =="N": break
            else:
                input("\nDatos invalidos intente nuevamente\nPresione Enter para continuar")

carga_persona()