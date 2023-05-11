import math
def cuadrado(base,altura):
    return base * altura

def circulo(radio):
    return 3.14 * math.pow(radio,2)
    
base=int(input("Ingrese base: "))
altura=int(input("Ingrese altura: "))
print(cuadrado(base,altura))
radio=int(input("Ingrese el radio del circulo: "))
print(circulo(radio))