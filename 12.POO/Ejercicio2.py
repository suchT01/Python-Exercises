class Resolver():
    def solver(self,x,n):
        self.x=x
        self.n=n
    def hacer(self):
        import math
        print("La broma es: ",math.pow(self.x,self.n))

hola=Resolver()
hola.solver(5,2)
hola.hacer()