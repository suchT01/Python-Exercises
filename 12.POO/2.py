class Fabrica:
    def __init__(self,tiempo,nombre,ruedas):
        self.tiempo=tiempo
        self.nombre=nombre
        self.ruedas=ruedas
        print("Se creo el auto:",self.nombre)
    def __str__(self):
        return "{}({})".format(self.nombre,self.tiempo)
class Listado:
    autos=[]
    def __init__(self,autos=[]):
        self.autos=autos
    def agregar(self,x):
        self.autos.append(x)
    def visualizar(self):
        for x in self.autos:
            print(x)

a = Fabrica(10,"Jose",4)
l=Listado([a])
l.visualizar()