# alumno: Angel Gabriel Saucedo
# Algoritmos y Programacion - B1
###################################################
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

turno = Cola()
for i in range(10): turno.encolar(i); print(f"paciente {i} agregado, cola actualizada {turno.clientes}")
for i in range(6): turno.desencolar(False); print(f"paciente {i} atendido, cola actualizada {turno.clientes}")
for i in range(10, 13): turno.encolar(i); print(f"paciente {i} agregado, cola actualizada {turno.clientes}")
print("Turnos: ",turno.clientes)