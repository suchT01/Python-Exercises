

class clase:
    def __init__(self,nombre) -> None:
        self.nombre=nombre
        print('Se ha generado la instancia:',self.nombre)

    def __del__(self):
        print('Se ha eliminado la instancia:',self.nombre)

obj1=clase('Uno')
print("Direccion de memoria de instancia {} ".format(obj1.nombre),id(obj1))

obj2=clase('Dos')
print("Direccion de memoria de instancia {} ".format(obj2.nombre),id(obj2))