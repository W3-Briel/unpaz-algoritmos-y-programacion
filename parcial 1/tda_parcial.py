class Pila:
 
    # Definimos el contructor   
    def __init__(self):
        # Inicializamos una 'pila vacía', el elemento contenedor es del
        # tipo de dato lista, donde se irán apilando los elementos.  
        self.lista = []
    
    # Método  que agrega un nuevo elemento a la pila (lista)    
    def apilar(self,item):
        self.lista.append(item)
        #print(f"Elemento apilado ") 
        
    # Método  que quita el último elemento ingresado de la pila (lista)
    def desapilar(self):
        if self.vacia():
            print("No se puede desapilar la pila está vacía")
        else:
            # pop retorna el elemento eliminado
             return self.lista.pop()
         
     # Método  que controla si la lista está vacía
    def vacia(self):
        if len(self.lista)==0:           
            return True
        else:           
            return False
    
    # Muestra de forma en forma de pila todos los elementos
    def mostrar(self):
        if not self.vacia():
            for i in self.lista[::-1]:
                print(f"[{str(i):^10}]")
            print()
        else:
            print("Pila vacía")
            

#Modificacion Creamos la funcion que devuelve el largo
    def largo(self):
        return len(self.lista)
        

class Cola:
    """ Representa a una cola, con operaciones de encolar y desencolar.
        El primero en ser encolado es también el primero en ser desencolado.
    """
    def __init__(self):
        """ Crea una cola vacía. """
        # La cola vacía se representa por una lista vacía
        self.lista_cola=[]
    
    def encolar(self, x):
        ''' Agrega el elemento x como último de la cola.  '''
        self.lista_cola.append(x)
        
    
    def desencolar(self):
        ''' Elimina el primer elemento de la cola y devuelve su
        valor. Si la cola está vacía envia un mensaje de cola vacia. '''
        
        if self.es_vacia():
            print("La cola está vacía")
        else:
            # pop retorna el elemento eliminado
            return self.lista_cola.pop(0)
            
    def es_vacia(self):
        ''' Devuelve True si la cola esta vacía, False si no. '''
        return self.lista_cola == []
    
    def mostrar(self):
        if self.es_vacia():
            print("Cola vacía")
        else:
            print(self.lista_cola)
        
     
# Modificacion Creamos la funcion que devuelve el largo
    def largo(self):
        return len(self.lista_cola)



'''        
   
# Creamos (Instanciamos) el objeto pila_numeros de la clase Pila
pila_numeros = Pila()

# Aplilamos (Agregamos) los elementos utilizando el Método  apilar
pila_numeros.apilar(1)

# Desapilamos (Quitamos) el último elemento agregado de la lista (pila)
pila_numeros.desapilar()

# Creamos (Instanciamos) el objeto cola_banco de la clase Cola
cola_banco = Cola()

# Encolamos (Agregamos) los elementos utilizando el Método encolar
cola_banco.encolar(10)
cola_banco.encolar(11)
cola_banco.encolar(12)

# Desencolamos (Atendemos) el primer cliente agregado a la cola
cola_banco.desencolar()
cola_banco.encolar(13)

# Muestra los lista_cola faltantes y la posición en la cola 
cola_banco.mostrar()

'''



