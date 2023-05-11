from math import sqrt
a=float(input("Ingrese variable a: "))
b=float(input("Ingrese variable b: "))
c=float(input("Ingrese variable c: "))
x1=0
x2=0
if ((b**2)-(4*a*c)) < 0 :
    print("No se puede realizar")
else:
    x1=(-b+sqrt((b**2)-(4*a*c)))/(2*a)
    x2=(-b-sqrt((b**2)-(4*a*c)))/(2*a)
print("Solucion 1:",x1)
print("Solucion 2:",x2)