lista=[]
pares=[]
impares=[]
def agregar():
    cantidad=int(input("Cuantos numeros deseas agregar: "))
    for i in range(cantidad):
        numero=int(input("El {} numero es: ".format(i+1)))
        lista.append(numero)

def orden():
    for i in lista:
        if i%2==0:
            pares.append(i)
        else:
            impares.append(i)
    pares.sort()
    impares.sort()
agregar()
print(lista)
orden()
print(pares)
print(impares)