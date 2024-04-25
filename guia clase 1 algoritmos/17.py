# alumno: Angel Gabriel Saucedo
# Algoritmos y Programacion - B1

############ ESTRUCTURAS ITERATIVAS WHILE ############

##17 Escribir un programa que muestre números del 0 al 30 uno debajo de otro. 
## ● Cuando los números sean 3, 8, 17, 26 debe mostrar el mensaje “saltando 
## instrucciones con(xxxxxxxxxxxxx el nombre de la instrucción que permite realizar 
## saltos en un bucle) llegue al número 3 o 8 o 17 o 26 ” 
## ● Cuando los números sean mayor a 25 debe preguntar si continúa o sale del conteo 
## (por ejemplo presione Presione: 'S' para salir , cualquier otra tecla para continuar) 
## ○ Si presiona cualquier tecla el programa seguirá su curso 
## ○ Si presiona S, terminará el programa, antes de terminar debe mostrar a qué 
## número de conteo llegó.

iterar = 0
while iterar <= 30:
    if iterar in (3, 8, 17):
        print("XXXXXXXXXSALTANDO INTRUCCIONXXXXXXXXXX")
    elif iterar > 25:
        match input("Presione: 'S' para salir , cualquier otra tecla para continuar; ").upper():
            case "S": print("saliendo del programa..."); break
            case _:
                if iterar == 26: print("XXXXXXXXXSALTANDO INTRUCCIONXXXXXXXXXX");iterar +=1; continue
                print(iterar); iterar +=1; continue
    else:
        print(iterar)
    iterar +=1