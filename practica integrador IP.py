import random as ram
import time

#Variables
diccionario= 'qwertyuiopasdfghjklñzxcvbnm1234567890'

categorias= {
    "camisas": 'camisas,camisetas, camisas de vestir, camisas informales, camisas de manga corta, manga larga',
    "pantalones": 'pantalones vaqueros, pantalones chinos, pantalones de vestir, pantalones cortos',
    "Vestidos": 'vestidos casuales, vestidos de cóctel, vestidos de noche, vestidos formales, vestidos estampados',
    "Trajes": 'trajes de dos piezas, trajes de tres piezas, trajes formales, trajes de oficina',
    "Ropa de abrigo": 'abrigos, chaquetas, chaquetones, gabardinas, chalecos',
    "Ropa deportiva": 'camisetas deportivas, pantalones deportivos, sudaderas, leggings deportivos, ropa de yoga',
    "Ropa de dormir": 'pijamas, camisones, batas, pantalones de pijama, conjuntos de dormir',
    "Accesorios": 'sombreros, gorras, bufandas, guantes, cinturones, joyas, bolsos'
}
catalogo = set()

## cargamos el catalogo con todos los elementos de las categorias
for i in categorias:
    for x in categorias[i].split(","):
        catalogo.add(x.strip())

###
#Listas
carrito=[]
##Funciones
def generador_con(diccionario,largo_con):
    #Genero la contraseña con valores aleatorios
    password=[]
    for i in range(largo_con):
        password.append(ram.choice(diccionario))

    return ''.join(password)

## bloquear un minuto
def bloquear():
    for segundos in range(0,60):
        print(f'0:{segundos}', end="\r")  
        time.sleep(1)


def verificar_con(mostrar_con):
    #Verifico si la contraseña ingresada es la misma que tiene el usuario y si pasa el limite de intentos que espere un minuto
    contador = 5
    while True:
        intento_verificar=(input('Ingrese su contraseña: '))
        if intento_verificar != mostrar_con:
            print('Contraseña incorrecta')
            contador -= 1
            if contador == 0:
                print('Excedió el limite de intentos. Deberá esperar un minuto.')
                bloquear()
                print('Puede volver a intentarlo.')
                print()
                contador = 5
        else:
            break
    return 'Contraseña correcta'


###
def carrito_productos():
    while True:
        contador= 5
        
        productos_elegidos=input('Ingrese el producto que quiere añadir: ')
        while productos_elegidos not in catalogo:
            print('El producto ingresado no se encuentra en el catalogo, ingrese otro.')
            productos_elegidos=input('Ingrese el producto que quiere añadir: ')
            contador-= 1
            if contador == 0:
                print('Excedió el limite de intentos. Deberá esperar un minuto.')
                bloquear()
                print('Puede volver a intentarlo.')
                print()
                contador = 5
            
            if productos_elegidos in catalogo: break

        while True:
            cantidad_producto= int(input(f'Ingrese la cantidad que quiere llevar de {productos_elegidos}: '))
            
            if cantidad_producto< 0:
                contador-= 1
                if contador == 0:
                    print('Excedió el limite de intentos. Deberá esperar un minuto.')
                    bloquear()
                    print('Puede volver a intentarlo.')
                    print()
                    contador = 5
            else:
                break
        
        for i in range(cantidad_producto):
            carrito.append(productos_elegidos)

        match input("seguir agregando productos? (si) (no): ").lower():
            case "no": break
            case "si": continue

def ver_carrito():
    detalle_carrito = []
    productos_agregados = []
    
    for producto in carrito:
        if producto in productos_agregados: continue
        for ca in categorias:
            if producto in categorias[ca]:
                detalle_carrito.append({"categoria":ca,"cantidad":carrito.count(producto),"producto":producto})
                productos_agregados.append(producto)
                break
    
    print(detalle_carrito)

def borrar_productos():
    borrador=input('Ingrese que elemento quiere borrar: ')

    for i in carrito:
        if i == borrador:
            print(f'Se ha eliminado del carrito: {borrador}')
            carrito.remove(i)


def metodos_de_pago():
        print('Ingrese de que forma va a pagar. ')
        print("""-Con efectivo tiene 10(%)(diez) de descuento,
                -Tarjeta: Cubre el programa ahora 3 (12(%) de interés) ,6 (18(%) de interés) y 12 (36(%) de interés). 
                -Bitcoin: Mismo precio""")
        pago=input('Ingrese de que forma va a pagar: ').lower()
        if pago == "efectivo":
            print("tendras un descuento de 10%")
        elif pago == 'bitcoin':
            print('pagará el mismo precio.')
        elif pago =='tarjeta':
            dia = input('Ingrese el dia que realiza la compra: ').capitalize()
            
            tarjetas = {"Domingo": "VISSA BNNA 15%",
                        "Lunes": "MASTERCARD PRV 20%",
                        "Martes": "CENNSOCUD MNP 15%",
                        "Miércoles": "CLARESEN KFC 30%",
                        'Jueves': "OFFIOTA LUCRA 20%",
                        'Viernes': "TREVVI CIR 10%",
                        'Sábado': "PUETRA COM 5%"}

            print(f"el dia {dia} con la tarjeta {tarjetas[dia]} de descuento")

        

    
       

##Def's generador y verificador de contraseña
print('Para ingresar a la tienda primero debe generar una clave')
largo_con=int(input('Ingrese el largo de su contraseña a generar: '))

mostrar_con=(generador_con(diccionario,largo_con))
print(f'su contraseña generada es: {mostrar_con}')

var_verificar=verificar_con(mostrar_con)
print(var_verificar)


####


##agregar productos



def menu():
    while True:    
        print(f'\n{10* "*"}MENU{10* "*"} \n')
        opciones=int(input("""Ingrese la opcion que quiera realizar: 
        1.Agregar productos al carrito
        2.Ver productos del carrito 
        3.Eliminar producto/s 
        4.Seleccionar medio de pago
        5.Salir y cerrar
        Opción: """))
        if opciones == 1:
            carrito_productos()
        elif opciones== 2:
            if carrito == []:
                print("no hay nada en carrito para mostrar")
                continue
            ver_carrito()
        elif opciones== 3:
            if carrito == []:
                print("no hay nada en carrito para borrar")
                continue
            borrar_productos()
        elif opciones== 4:
            print('medio de pago')
            metodos_de_pago()
        elif opciones== 5:
            print('Fin del programa')
            break
        else:
            print('Ingrese una opcion válida')

menu()