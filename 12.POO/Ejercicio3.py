class Calculadora():
    def __init__(self):
        self.dato1=int(input("Primer valor: "))
        self.dato2=int(input("Segundo valor: "))
    def suma(self):
        print("La suma de los valores es:",self.dato1+self.dato2)
    def resta(self):
        print("La resta de los valores es:",self.dato1-self.dato2)
    def multiplicar(self):
        print("La multiplicacion de los valores es:",self.dato1*self.dato2)
    def division(self):
        print("La division de los valores es:",self.dato1/self.dato2)

datos=Calculadora()
datos.suma()