class NodoLo:
    def __init__(self,datoInicial):
        self.dato = datoInicial
        self.siguiente = None

    def obtenerDato(self):
        return self.dato

    def obtenerSiguiente(self):
        return self.siguiente

    def asignarSiguiente(self,nuevosiguiente):
        self.siguiente = nuevosiguiente

class ListaOrdenada:

    def __init__(self):
        self.cabeza = None
    
    def estaVacia(self):
        return self.cabeza == None

    def tamano(self):
        actual = self.cabeza
        contador = 0
        while actual != None:
            contador = contador + 1
            actual = actual.obtenerSiguiente()
        return contador

    def remover(self,item):
        actual = self.cabeza
        previo = None
        encontrado = False
        while not encontrado and actual != None:
            
            if actual.obtenerDato() == item:
                encontrado = True
            else:
                previo = actual
                actual = actual.obtenerSiguiente()        
        if actual != None:
            if previo == None:
                self.cabeza = actual.obtenerSiguiente()
            else:
                previo.asignarSiguiente(actual.obtenerSiguiente())
    
    def buscar(self,item):
        actual = self.cabeza
        encontrado = False
        detenerse = False
        while actual != None and not encontrado and not detenerse:
            if actual.obtenerDato() == item:
                encontrado = True
            else:
                if actual.obtenerDato() > item:
                    detenerse = True
                else:
                    actual = actual.obtenerSiguiente()

        return encontrado

    def agregar(self,item):
        actual = self.cabeza
        previo = None
        detenerse = False
        while actual != None and not detenerse:
            if actual.obtenerDato() > item:
                detenerse = True
            else:
                previo = actual
                actual = actual.obtenerSiguiente()

        temp = NodoLo(item)
        if previo == None:
            temp.asignarSiguiente(self.cabeza)
            self.cabeza = temp
        else:
            temp.asignarSiguiente(actual)
            previo.asignarSiguiente(temp)

    def ver(self):
        print("[",end="")
        if self.estaVacia:            
            actual = self.cabeza
            while actual != None:
                 print(actual.dato,end="")
                 actual = actual.obtenerSiguiente()
                 if actual != None:
                    print(end=',')
            print("]")
        else:
            print('[]')
        return

#Modulo Nuevo
    def metodo_nuevo(self,x):
        actual = self.cabeza
        contador = 0
        while actual != None:
            if contador == x:
                return actual.dato
            actual = actual.obtenerSiguiente()
            contador += 1
        return None
    
    def borrar_lista(self):
        self.cabeza= None