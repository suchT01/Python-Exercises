class Fabrica():
    def __init__(self,llantas,color,precio):
        self.llantas=llantas
        self.color=color
        self.precio=precio
    def __str__(self):
        return """\n
        Llantas:\t{}
        Color:\t\t{}
        Precio:\t\t{}
        """.format(self.llantas,self.color,self.precio)
class Moto(Fabrica):
    def datos(self):
        pass
    
class Carro(Fabrica):
    def datos(self):
        pass

moto=Moto(2,"Rojo",12000)
carro=Carro(4,"Verde",30000)
print(moto,carro)