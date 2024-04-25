class Nodo:
    def __init__(self,datoInicial):
        self.dato = datoInicial
        self.siguiente = None
    
    #metodos
    def obtener_dato(self):
        return self.dato
    def obtener_siguiente(self):
        return self.siguiente
    def asignar_siguiente(self,nuevoSiguiente):
        self.siguiente = nuevoSiguiente

class Lista_ordenada:
    def __init__(self):
        self.cabeza = None # la lista define la cabeza, no los nodos.
    # metodos

    def esta_vacia(self):
        return self.cabeza == None
    
    def tamaño(self):
        actual = self.cabeza
        contador = 0
        while actual != None:
            contador += 1
            actual = actual.obtener_siguiente()
        return contador
    def remover(self,item):
        actual = self.cabeza
        previo = None
        encontrado = False
        while not encontrado and actual != None:
            if actual.obtener_dato() == item: encontrado = True
            else: previo = actual; actual = actual.obtener_siguiente()

        if actual != None:
            if previo == None: self.cabeza = actual.obtener_siguiente()
            else: previo.asignar_siguiente(actual.obtener_siguiente())

    def buscar(self,item):
        actual = self.cabeza
        encontrado = False
        detenerse = False
        while actual != None and not encontrado and not detenerse:
            if actual.obtener_dato() == item:
                encontrado = True
            else:
                if actual.obtener_dato() > item: detenerse = True
                else: actual = actual.obtener_siguiente()
        return encontrado

    def ver(self):
        print("cabeza", end= "->")
        if not self.esta_vacia():
            actual =  self.cabeza
            while actual != None:
                print(actual.dato, end ="->")
                actual = actual.obtener_siguiente()
        print("None")
    

    def agregar(self,item):
        actual = self.cabeza
        previo = None
        detenerse = False
        while actual != None and not detenerse:
            if actual.obtener_dato() > item: detenerse = True
            else: previo = actual; actual = actual.obtener_siguiente()

        temp = Nodo(item)
        if previo == None:
            temp.asignar_siguiente(self.cabeza); self.cabeza = temp
        else: temp.asignar_siguiente(actual); previo.asignar_siguiente(temp)

class Lista_no_ordenada:
    def __init__(self):
        self.cabeza = None # la lista define la cabeza, no los nodos.
    # metodos

    def esta_vacia(self):
        return self.cabeza == None
    def agregar(self,item):
        temp = Nodo(item)
        temp.asignar_siguiente(self.cabeza)
        
        self.cabeza = temp ## el nuevo objeto nodo sera cabeza.
    
    def tamaño(self):
        actual = self.cabeza
        contador = 0
        while actual != None:
            contador += 1
            actual = actual.obtener_siguiente()
        return contador
    def buscar(self,item):
        actual = self.cabeza
        encontrado = False
        while actual != None and not encontrado:
            if actual.obtener_dato() == item: encontrado = True
            else: actual = actual.obtener_siguiente()
        return encontrado
    def remover(self,item):
        actual = self.cabeza
        previo = None
        encontrado = False
        while not encontrado and actual != None:
            if actual.obtener_dato() == item: encontrado = True
            else: previo = actual ; actual = actual.obtener_siguiente()
        
        if actual != None:
            if previo == None: self.cabeza = actual.obtener_siguiente()
            else: previo.asignar_siguiente(actual.obtener_siguiente())
    def ver(self):
        print("cabeza", end= "->")
        if not self.esta_vacia():
            actual =  self.cabeza
            while actual != None:
                print(actual.dato, end ="->")
                actual = actual.obtener_siguiente()
        print("None")
    def anexar(self, item):
        temp = Nodo(item)
        actual = self.cabeza
        previo = None
        while actual != None:
            previo = actual
            actual = actual.obtener_siguiente()
        if previo == None: self.agregar(item)
        else: temp = Nodo(item); previo.asignar_siguiente(temp)