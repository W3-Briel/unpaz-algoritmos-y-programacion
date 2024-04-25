# alumno: Angel Gabriel Saucedo
# Algoritmos y Programacion - B1

######################## FUNCIONES RECURSIVAS #########################
# Implementar una función para calcular la potencia dado dos números enteros, el primero
# representa la base y el segundo el exponente.

def potencia_recursiva(base,exponente):
    if base == 1 or base == 0 or exponente == 1:
        return base
    elif exponente == 0 and base != 0:
        return 1
    else:
        return base * potencia_recursiva(base,exponente-1)

#input - excepciones
while True:
    try:
        numero_base = int(input("ingresa una base: "))
        if numero_base < 0: print("uno positivo por favor...");continue
        while True:
            try:
                numero_exponente = int(input("ingresa un exponente: "))
                if numero_exponente < 0: print("uno positivo por favor...");continue
                else: break
            except ValueError:
                print("solo numeros!!, intenta denuevo")
        break
    except ValueError:
        print("solo numeros!!, intenta denuevo"); continue
    
print(potencia_recursiva(numero_base,numero_exponente))