with open("este_es_el_ejercicio_1.txt","a+") as file:
    file.write("Este es el ejercicio 1")
    file.seek(0)
    print(f"codificacion: {file.encoding}, contenido del archivo:\n\n{file.read()}")