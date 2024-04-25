class Pila():
    # constructor
    def __init__(self):
        self.lista = []

    #metodos
    def apilar(self,item,info):
        self.lista.append(item)
        if info: print(f"\nElemento {item} apilado, lista actualizada: {self.lista}")

    def mi_pila(self):
        for apilado in reversed(self.lista):
            print(f"[\t {apilado}   \t]")

    def desapilar(self,info):

        if info:
            if self.vacia(): print("\nNo se puede desapilar la lista esta vacia")
            else: print(f"\nElemento {self.lista.pop()} desapilado, lista actualizada: {self.lista}")

        if not self.vacia(): return self.lista.pop()

    def tamanio(self):
        print(f"\nLa pila tiene {len(self.lista)} elementos")

    def vacia(self):
        if len(self.lista) == 0: return True; return False

    def limpiar(self,info):
        self.lista.clear()
        if info: print("\nLista vaciada")

class Cola():
    #constructor
    def __init__(self):
        self.clientes = []
    
    #metodos
    def encolar(self,x):
        self.clientes.append(x)
    
    def es_vacia(self):
        return self.clientes == []
    
    def desencolar(self,info):
        if info:
            mensaje = "la cola esta vacia, no hay mas clientes" if self.es_vacia() else f"\nCliente {self.clientes.pop(0)} atendido (desencolado), cola actualizada: {self.clientes}"
            return mensaje

        if not self.es_vacia(): return self.clientes.pop(0)